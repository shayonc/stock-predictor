import pandas

if __name__ == '__main__':
    
    columns = ['date', 'close', 'volume']
    df = pandas.read_csv('TSLA.csv', names=columns, sep=',')

    columns2 = ['date', 'mean', 'sd']
    df2 = pandas.read_csv('sentiment_values.csv', names=columns2, sep=',')

    merged = pandas.merge(df, df2, on=['date'])
            
    with open('final.csv', 'w') as file:
        merged.to_csv('final.csv', sep=',')
