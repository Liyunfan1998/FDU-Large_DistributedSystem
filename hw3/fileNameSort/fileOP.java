import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;

import java.util.Random;

import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.io.WritableComparable;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.SequenceFileInputFormat;
import org.apache.hadoop.mapreduce.lib.map.InverseMapper;
import org.apache.hadoop.mapreduce.lib.output.*;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class fileOP {

    //继承LongWritable.Comparator，对key进行倒序
    private static class DecreasingComparator extends LongWritable.Comparator {
        public int compare(WritableComparable a, WritableComparable b) {
            return -super.compare(a, b);
        }

        public int compare(byte[] b1, int s1, int l1, byte[] b2, int s2, int l2) {
            return -super.compare(b1, s1, l1, b2, s2, l2);
        }
    }

    //继承Mapper，对数据进行拆分，其中<Object,Text>为数据的输入类型，<LongWritable, Text>为数据的输出类型
    //由于要按照文件大小降序，所以将文件大小作为key（hadoop里是按照key排序的）
    public static class fileNameMapper extends Mapper<Object, Text, LongWritable, Text> {

        //删除String[]里面的空字符串，JAVA里面完成这个任务真的好复杂啊。。。。
        private String[] removeArrayEmptyTextBackNewArray(String[] strArray) {
            List<String> strList = Arrays.asList(strArray);
            List<String> strListNew = new ArrayList<>();
            for (int i = 0; i < strList.size(); i++) {
                if (strList.get(i) != null && !strList.get(i).equals("")) {
                    strListNew.add(strList.get(i));
                }
            }
            String[] strNewArray = strListNew.toArray(new String[strListNew.size()]);
            return strNewArray;
        }

        private final static LongWritable fileSize = new LongWritable(0);
        private Text fileType = new Text();

        //map方法的重写，将数据拆分成<fileSize,fileType>的形式，将数据以<Text,IntWritable>的形式传送到reduce
        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            //在处理字符串输入的过程中由于是中文会产生乱码，而hadoop又不支持UTF-8，所以用GBK解析
            String line = new String(value.getBytes(), 0, value.getLength(), "GBK");
            String[] tokensList = line.split("   ");
            tokensList = removeArrayEmptyTextBackNewArray(tokensList);
            tokensList = tokensList[1].split(" ");
            tokensList = removeArrayEmptyTextBackNewArray(tokensList);
            long fileSize = Long.parseLong((tokensList[0]).replaceAll(",", ""));
            if (tokensList.length >= 3) {
                fileType.set(tokensList[1] + " " + tokensList[2]);
            } else {
                fileType.set(tokensList[1]);
            }
            //由于要按照文件大小降序，所以将文件大小作为key（hadoop里是按照key排序的）
            context.write(new LongWritable(fileSize), fileType);

        }
    }

    //继承Reducer，通过shuffle阶段获得Map处理后的<fileSize,fileType>的值，对数据直接以<fileSize,fileType>的形式输出
    //其中<LongWritable, Text>为输入的格式,<LongWritable, Text>为输出的格式
    public static class IntSortReducer extends Reducer<LongWritable, Text, LongWritable, Text> {
        private IntWritable result = new IntWritable();

        public void reduce(LongWritable key, Text value, Context context)
                throws IOException, InterruptedException {
            context.write(key, value);
        }
    }

    public static void sortFileBySize(Path input, Path output, Configuration conf)
            throws IOException, InterruptedException, Exception {
//        Path tempDir = new Path("wordcount-temp"); //定义一个临时目录

        //建立job任务
        Job job = Job.getInstance(conf, "file sort by size");
        //配置job中的各个类
        job.setJarByClass(fileOP.class);
        job.setMapperClass(fileNameMapper.class);
        //combine方法是在reduce之前对map处理结果的一个局部汇总，一般有几个map就会有几个combine

        job.setCombinerClass(IntSortReducer.class);
        job.setReducerClass(IntSortReducer.class);
        //设置输入输出格式
        job.setOutputKeyClass(LongWritable.class);
        job.setOutputValueClass(Text.class);
        //用DecreasingComparator实现倒序
        job.setSortComparatorClass(DecreasingComparator.class);
        //设置输入输出路径
        FileInputFormat.addInputPath(job, input);
        FileOutputFormat.setOutputPath(job, output);
        //由任务是否完成而选择是否正常退出程序
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }

    public static void main(String[] arg) throws Exception {
        Configuration conf = new Configuration();
        //从命令行中获取输入输出的路径
        Path input = new Path(arg[0]);
        Path output = new Path(arg[1]);
        //执行mapreduce方法
        sortFileBySize(input, output, conf);

    }

}
