export PATH="/usr/local/opt/gettext/bin:$PATH"
export LDFLAGS="-L/usr/local/opt/gettext/lib"
export CPPFLAGS="-I/usr/local/opt/gettext/include"

export WEIXIN_APPID="wxda26da7da787099e"
export WEIXIN_MCHID="0"
export WEIXIN_PAY_SECRET="0"
export WEIXIN_NOTIFY_URL="0"
# JAVA_HOME=`/usr/libexec/java_home`
JAVA_HOME='/Library/Java/JavaVirtualMachines/jdk1.8.0_91.jdk/Contents/Home'
export JAVA_HOME

#export CLASSPATH=$CLASSPATH:$JAVA_HOME
export CLASSPATH="$PATH:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$CLASSPATH"
export PATH=$PATH:$JAVA_HOME/bin:$JAVA_HOME/jre/bin
export CLASSPATH=$JAVA_HOME/lib:$CLASSPATH
#export HADOOP_HOME="/usr/local/Cellar/hadoop/3.1.2/libexec"
#export HBASE_HOME="/usr/local/Cellar/hbase/1.2.9"

export HADOOP_HOME=/Users/liyunfan/hadoop-2.8.5
export HBASE_HOME=/Users/liyunfan/hbase-2.0.5



export HADOOP_COMMON_HOME=$HADOOP_HOME
#export CLASSPATH="$CLASSPATH:$HADOOP_HOME/share/hadoop/common/hadoop-common-3.2.0.jar:$HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-3.2.0.jar:$HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar:$CLASSPATH"



export PATH=$PATH:$JAVA_HOME/bin:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
export PATH=$PATH:$HBASE_HOME/bin:$HBASE_HOME/sbin

export HADOOP_OPTS="$HADOOP_OPTS -Djava.library.path=$HADOOP_HOME/lib/native"

export HADOOP_ROOT_LOGGER=DEBUG,console
export SPARK_HOME=/Users/liyunfan/spark-2.4.1-bin-hadoop2.7

export PATH=$PATH:$SPARK_HOME/bin
export CLASSPATH=$CLASSPATH:$HADOOP_HOME:$HBASE_HOME

#export PATH=$PATH:/usr/local/opt/hbase/bin
#export HBASE_CONF=/usr/local/Cellar/hbase/1.2.9/libexec/conf
#export HADOOP_CONF_DIR=/usr/local/Cellar/hadoop/3.1.2/libexec/etc/hadoop
export HADOOP_ROOT_LOGGER=DEBUG,console

export HADOOP_CONF_DIR=/Users/liyunfan/hadoop-2.8.5/etc/hadoop
export HBASE_CONF=/Users/liyunfan/hbase-2.0.5/conf



# added by Anaconda3 2019.03 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<
# added by Miniconda3 4.5.12 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/Users/liyunfan/miniconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/Users/liyunfan/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/liyunfan/miniconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/Users/liyunfan/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<
export PATH="/usr/local/opt/icu4c/bin:$PATH"
export PATH="/usr/local/opt/icu4c/sbin:$PATH"
export LDFLAGS="-L/usr/local/opt/icu4c/lib"
export CPPFLAGS="-I/usr/local/opt/icu4c/include"
