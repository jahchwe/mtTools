# mtTools
For the simple tasks that nonetheless take clicks. 

## Operation
```python 
python mtTools.py {function} 
```
## Dependencies
• pandas
## webMT tools
Tools for use with the webMT server. 
### getData(password, responsePath, destination)
>
> Retrieves data at the given server path and saves at local destination. 
>
> responsePath should be specified from within the responses folder. For example, if you wanted to get the ratings from a ratings study named emotionReg, the path would be specified as **ratings/emotionReg/ratings**. You can also retrieve Screener, demo, and consent, etc.
>
> destination should be a local directory. 

### concatResponses(dataPath, outputFilename)
> 
> Concatenates final csv's into one csv. NOTE: will only concatenate csv files that start with the string "final". 
>
> Output csv will be placed into same directory as dataPath. 

## localMT
Coming soon...(?)

### makeMT (procedural way to make the csv's for localMT studies)
