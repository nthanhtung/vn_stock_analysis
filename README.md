
---------
# setup
## 1. manual install wheel file in folder /dist
file name: TA_Lib-0.4.21-cp39-cp39-win_amd64.whl
## 2. install all library in requirements.txt
pip install -r requirements.txt
## 3. download data & template power bi report
link: https://drive.google.com/drive/folders/1bCgw5kKVVOLYC3QKsSSrR3_KIb1JAmn_?usp=sharing
## 4. edit data path 
* in power bi: parameter in utility
* in python code: /test/x.py
## 5. run python script in folder /test to get daily data
* 1. script switch_dir.py
* 2. script x.py : only need to load daily data
* Note: you can build this project as wheel file, then install vn_stock_analysis wheel file, then you don't need to run switch_dir.py
---------
below part is in progress to be completed
# use case

## stock scan based on signal:
* technical analysis
* fundamental analysis

## stock correlation with relevant commodity:
* HPG with steel
* PNJ with gold
* PVS with VNindex

# data source

data source <br />
https://www.cophieu68.vn/export.php <br />
https://finfoapi-hn.vndirect.com.vn/stocks/adPrice?symbols=HOSE&fromDate=2015-01-01&toDate=2021-05-31 <br />
https://finfo-api.vndirect.com.vn/v3/stocks/financialStatement?secCodes=VNM&fromDate=2017-06-30&toDate=2019-06-30 <br />
stock price hourly last 5 day <br />
https://dchart-api.vndirect.com.vn/dchart/history?resolution=5&symbol=VNM&from=1620000000&to=1622893022 <br />
financial data year end, quarter end <br /> 
https://finfo-api.vndirect.com.vn/v3/stocks/balanceSheet?secCodes=VNM&fromDate=2019-01-01&toDate=2019-12-31 <br />
https://finfo-api.vndirect.com.vn/v3/stocks/financialStatement?secCodes=VNM&reportTypes=QUARTER&fromDate=2017-06-30&toDate=2019-06-30 <br />
stock price daily: https://finfoapi-hn.vndirect.com.vn/stocks/adPrice?symbols=VNM&fromDate=2015-01-01&toDate=2021-05-31 <br />

# example template

example template <br />

https://github.com/wilsonfreitas/awesome-quant <br />
https://pypi.org/project/finance-calculator/ <br />
https://indzara.com/stock-market-templates/ <br />
https://stackoverflow.com/questions/39501277/efficient-python-pandas-stock-beta-calculation-on-many-dataframes <br />


# E
	get data 20 y 1 shot
	get data this y daily
	VN data: higher prority
        firm finance statement
	    price & volume data
        stock symbal mapping: industry
    World data:
        US stock market
        Comodity price


# T
	technical analysis
	fundamental analysis
    benchmark analysis:
        industry
        regional, global
	backtest & strategy efficiency analysis
    stock correlation with relevant commodity
	

# L
	write semantic layer data to yearly file

-------

# design

text
diagram
sttm
report template: excel/power bi/web mockup

------------

market gap in stock trading analysis tool

    stock valuation tool:
        input:
            growth assumption
            market risk
    

    stock scan based on stock valuation


    industry benchmarking tool:
        p/e
        p/b
        beta
        vs us, asean


---------
# Discounted cash flow (DCF) valuation views the intrinsic value of a security
    cash flows actually paid to stockholders
        dividend discount model (DDM)
    cash flows available for distribution to shareholders
        free cash flow to the firm (FCFF)
        free cash flow to equity (FCFE)
        analysts consider free cash flow models to be more useful than DDMs in practice
        Free cash flows provide an economically sound basis for valuation
    market multiples

    practice
        residual income
        dividend discount
        discounted free cash flow
        FCFF models are used roughly twice as frequently as FCFE models
        Analysts like to use free cash flow as the return (either FCFF or FCFE)
            The company does not pay dividends.
            Free cash flows align with profitability within a reasonable forecast period with which the analyst is comfortable.




# Calculation

FCFF = CFO + Int(1 – Tax rate) – FCInv.

FCFE = CFO – FCInv + Net borrowing.

Equity value = Firm value – Market value of debt.

Dividing the total value of equity by the number of outstanding shares gives the value per share.

----------

WACC  =  (E/V x Re)  +  ((D/V x Rd)  x  (1 – T))

Where:

E = market value of the firm’s equity (market cap)
D = market value of the firm’s debt
V = total value of capital (equity plus debt)
E/V = percentage of capital that is equity
D/V = percentage of capital that is debt
Re = cost of equity (required rate of return)
Rd = cost of debt (yield to maturity on existing debt)
T = tax rate

Re  =  Rf  +  β  ×  (Rm − Rf)

Where:

Rf = the risk-free rate (typically the 10-year U.S. Treasury bond yield)
β = equity beta (levered)
Rm = annual return of the market


