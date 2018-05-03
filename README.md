# Facebook Personal Data Analysis

## Description
Facebook offers you the possibiity the download your personnal data. A tutorial on how to do so is available **[here](https://www.facebook.com/help/131112897028467)**.
The data is given in formats that are not directly open to visualization nor open to analysis. Here is a collection of Python tools that are extracting data from a personal archive.

This repository covers :
1. Facebook Messenger Conversation Data Extraction
2. 




### Facebook Messenger Conversation Data Extraction

The ``extraction_tool`` python script is composed of a function ``export_conv`` that creates a .txt and .csv from the html of a archive of Facebook conversation. 

To use it in your code :

``` 
import extraction_tool as et
```

and then call the function 

```
et.export_conv(('your_name', num_of_the_conv, path_to_conv_file)
```