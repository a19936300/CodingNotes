# 项目导入数据保存时使用分布式锁报异常

```
22:05:07.354 [Thread-2] INFO com.binbinxiu.aihushop.redisson.oneThread - 获取分布式锁成功-----org.redisson.RedissonLock@302daf3f
22:05:07.385 [Thread-2] INFO com.binbinxiu.aihushop.redisson.oneThread - 释放分布式锁成功-----org.redisson.RedissonLock@302daf3f
Exception in thread "Thread-1" java.lang.IllegalMonitorStateException: attempt to unlock lock, not locked by current thread by node id: 453486a2-e9c3-4ef8-ac33-734e2d75409b thread-id: 54
	at org.redisson.RedissonLock.lambda$unlockAsync$3(RedissonLock.java:578)
	at org.redisson.misc.RedissonPromise.lambda$onComplete$0(RedissonPromise.java:187)
	at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:578)
	at io.netty.util.concurrent.DefaultPromise.notifyListeners0(DefaultPromise.java:571)
	at io.netty.util.concurrent.DefaultPromise.notifyListenersNow(DefaultPromise.java:550)
	at io.netty.util.concurrent.DefaultPromise.notifyListeners(DefaultPromise.java:491)
	at io.netty.util.concurrent.DefaultPromise.setValue0(DefaultPromise.java:616)
	at io.netty.util.concurrent.DefaultPromise.setSuccess0(DefaultPromise.java:605)
	at io.netty.util.concurrent.DefaultPromise.trySuccess(DefaultPromise.java:104)
```

给的提示：当前线程的锁已经被释放，然后再去释放时就报了异常。


相似源代码：
```
public void run() {

    RLock lock = redissonClient.getLock("lock");
    try {
        boolean b = lock.tryLock(3, 1, TimeUnit.SECONDS);
        logger.info("获取分布式锁成功-----{}",lock);
        if(b){
            //执行save方法
            Thread.sleep(30);
        }
    } catch (Exception e) {
        //失败回滚
    }finally {
        logger.info("释放分布式锁成功-----{}",lock);
        if(lock.isHeldByCurrentThread()){
            lock.unlock();
        }
    }
}

```

搞不懂的地方：

```
if(lock.isHeldByCurrentThread()){
   lock.unlock();
}
```

我已经判断了当前线程是否持有，然后才释放，为什么还会报错？难道是刚进入if分支就过期了，但是我延长了持有锁的时间还是会出现这种问题。