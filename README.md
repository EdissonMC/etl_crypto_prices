# 📈 Crypto Market ETL & Analytics Project

This project implements a basic **ETL pipeline (Extract, Transform, Load)** to retrieve, clean, analyze, and visualize cryptocurrency data using real-time information from the **CoinMarketCap API**. The goal is to showcase skills in data engineering, statistical analysis, and clean project structure using Python.

---

## 🚀 Project Overview

1. **Extract**: Connects to CoinMarketCap (sandbox environment) and pulls market data for the top 100 cryptocurrencies.
2. **Transform**:
   - Cleans and reshapes the raw data.
   - Detects and analyzes **outliers** using Interquartile Range (**IQR**) method.
3. **Load**: Saves the processed data locally to a CSV file (`crypto_data.csv`) for further analysis and plotting.
4. **Visualization**:
   - Price distribution plots with outlier highlighting.
   - Comparison between normal values and detected outliers using `matplotlib` and `seaborn`.

---

## 🧠 Tech Stack

- `Python 3.10+`
- `Pandas` and `NumPy` for data manipulation
- `Seaborn` and `Matplotlib` for visualizations
- `Requests` for API interaction
- `Poetry` for dependency management
- `dotenv` for secure API key management

---

## 🛠️ Project Structure


---

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/crypto-etl-project.git
   cd crypto-etl-project

2. Install dependencies using Poetry:
    poetry install


3. Add your CoinMarketCap API key to a .env file:

    COINMARKETCAP_API_KEY=your_api_key_here

4. Run the pipeline:
    poetry run python main.py


👨‍💻 Author
Edisson Mogollon
Software Engineer & Master's student in Computer Science (AI & Deep Learning).
Passionate about machine learning, data engineering, and real-world applications of generative AI.

🧪 License
MIT License — Feel free to use, modify, and build upon this project.