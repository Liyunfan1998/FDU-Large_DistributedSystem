import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;

public class wordcount {

    //继承Mapper，对数据进行拆分，其中<Object,Text>为数据的输入类型，<Text,IntWritable>为数据的输出类型
    public static class TokenizerMapper extends Mapper<Object, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();

        //map方法的重写，将数据拆分成<word,one>的形式，将数据以<Text,IntWritable>的形式传送到reduce
        public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
            StringTokenizer it = new StringTokenizer(value.toString(), ".\n\r");
            while (it.hasMoreTokens()) {
                String nextToken = it.nextToken();
                //由于文件中后缀名长度都不超过5，因此在这里做个判断，只选后缀名做count
                if (nextToken.length() > 5) {
                    continue;
                }
                word.set(nextToken);
                context.write(word, one);
            }
        }
    }

    //继承Reducer，通过shuffle阶段获得Map处理后的<word,one>的值，对数据进行汇总合并后以<word,result>的形式输出
    //其中<Text, IntWritable>为输入的格式,<Text,IntWritable>为输出的格式
    public static class IntSumReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
        private IntWritable result = new IntWritable();

        //重写reduce方法，对词频进行统计，其中输入的数据形式为<key,{1，1，1，1}>的形式
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            int sum = 0;
            //将相同的key的value值进行相加，得出词频结果
            for (IntWritable val : values) {
                sum = sum + val.get();
            }
            result.set(sum);
            context.write(key, result);
        }
    }

    public static void wordcountMapReduce(Path input, Path output, Configuration conf) throws IOException, InterruptedException, Exception {
        //建立job任务
        Job job = Job.getInstance(conf, "word count");
        //配置job中的各个类
        job.setJarByClass(wordcount.class);
        job.setMapperClass(TokenizerMapper.class);
        //combine方法是在reduce之前对map处理结果的一个局部汇总，一般有几个map就会有几个combine
        job.setCombinerClass(IntSumReducer.class);
        job.setReducerClass(IntSumReducer.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, input);
        FileOutputFormat.setOutputPath(job, output);
        //提交任务
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }

    public static void main(String[] arg) throws Exception {
        Configuration conf = new Configuration();
        //从命令行中获取输入输出的路径
        Path input = new Path(arg[0]);
        Path output = new Path(arg[1]);
        //执行mapreduce方法
        wordcountMapReduce(input, output, conf);
    }
}
