import pandas as pd
import plotly.express as px

def data():
    path = input("Enter the full path to your CSV file: ")
    try:
        df = pd.read_csv(path)
        print("\n Dataset loaded successfully!")
        print(f"Available columns: {list(df.columns)}\n")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None
def chart():
    print("\nChoose chart type:")
    print("1. Line Chart")
    print("2. Bar Chart")
    print("3. Scatter Plot")
    print("4. Histogram")
    print("5. Pie Chart")
    return input("Enter your choice (1-5): ")
def generate(df, chart_type):
    if chart_type == '5':
        labels = input("Enter the column for labels (categorical): ")
        values = input("Enter the column for values (numeric): ")
        if labels in df.columns and values in df.columns:
            fig = px.pie(df, names=labels, values=values, title="Pie Chart")
        else:
            print("Invalid column names.")
            return
    else:
        a = input("Enter X-axis column: ")
        b = input("Enter Y-axis column: ")
        if a not in df.columns or b not in df.columns:
            print("Invalid column names.")
            return
        if chart_type == '1':
            fig = px.line(df, x=a, y=b, title="Line Chart")
        elif chart_type == '2':
            fig = px.bar(df, x=a, y=b, title="Bar Chart")
        elif chart_type == '3':
            fig = px.scatter(df, x=a, y=b, title="Scatter Plot")
        elif chart_type == '4':
            fig = px.histogram(df, x=b, title="Histogram")
        else:
            print("Invalid chart type.")
            return
    fig.show()
def main():
    print("Welcome to the Interactive Data Visualization Tool")
    df = data()
    if df is not None:
        type = chart()
        generate(df, type)
if __name__ == "__main__":
    main()
