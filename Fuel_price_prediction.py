{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Fuel_price_prediction.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "BW4YGzitNK8-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f8cbce5c-c437-4413-f221-3ceee2512e4d"
      },
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "df = pd.read_csv(r'https://img1.wsimg.com/blobby/go/8c96521b-7ee0-4579-b983-c9c9fac1057e/downloads/FuelEconomy.csv?ver=1609666327321')\n",
        "X = df[['Horsepower']]\n",
        "X.shape\n",
        "y = df['Fuel Economy']\n",
        "#5 Split\n",
        "from sklearn.model_selection import train_test_split\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, random_state = 252)\n",
        "X_train\n",
        "from sklearn.linear_model import LinearRegression\n",
        "model = LinearRegression()\n",
        "model.fit(X_train, y_train)\n",
        "model.intercept_\n",
        "model.coef_\n",
        "y_pred = model.predict(X_test)\n",
        "from sklearn.metrics import mean_absolute_error\n",
        "\n",
        "mean_absolute_error(y_test, y_pred)\n"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1.1760176317464688"
            ]
          },
          "metadata": {},
          "execution_count": 1
        }
      ]
    }
  ]
}