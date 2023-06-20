import logging

class LogGen:
    @staticmethod
    def loggen():
        logger  = logging.getLogger("Test Login")
        fileHandler  = logging.FileHandler('.\\YourDesiredFolderName')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
```

`
You can pass the name of your test case as a parameter inside the *getLogger()* method.
The *filehandler* class will handle the your desired location for your logs.
*Formatter* method will make sure your logs are being stored following a proper format.
The *logger* variable will return the log at the end of the execution.


# Driver code

Now it's time to use that *loggen()* function.
Create another python file to add the driver code. Inside of this file,
import the *loggen* function by simply using this code `from log.logCapture import logGen`.
The code is basically for accessing the LogGen class which we created earlier. Then use the logging by just calling the *logger* variable.

Let's say we want to test a login page.
So you can add logs by using `logger.info("You desired massage")` right before the execution of the test case
or where ever you want. After executing the test cases,
you will see a log file has been created in your desired folder. The log should look something like this


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/l0l5wcqxjz2qcb5q3skr.png)

This is the output of my logs after executing the test cases. This is how my code looks like behind this


![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/su9g6zdgko1kwvjxo420.png)

You should be able to use log if you follow this procedure :)


> Thanks for reading. Pardon me for the mistakes I may have made as I am new to automation testing and still exploring everyday. I would be glad if it helps anyone. :)