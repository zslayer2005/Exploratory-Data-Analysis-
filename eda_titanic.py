
{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Titanic EDA Notebook\n",
    "Exploratory Data Analysis on Titanic dataset"
   ]
  },
  {
   "cell_type": "code",
#    "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "code",
#    "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('titanic.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
#    "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Summary statistics\n",
    "df.describe(include='all')\n",
    "df.info()\n",
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
#    "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Histograms and Boxplots\n",
    "df.hist(figsize=(12, 8), bins=20)\n",
    "plt.tight_layout()\n",
    "plt.show()\n",
    "\n",
    "for col in ['Age', 'Fare']:\n",
    "    sns.boxplot(x=df[col])\n",
    "    plt.title(f'Boxplot of {col}')\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
#    "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Correlation and Pairplot\n",
    "sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')\n",
    "plt.title('Correlation Matrix')\n",
    "plt.show()\n",
    "\n",
    "sns.pairplot(df[['Survived', 'Age', 'Fare', 'Pclass']], hue='Survived')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
#    "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Categorical analysis\n",
    "sns.countplot(x='Survived', data=df)\n",
    "plt.title('Survival Count')\n",
    "plt.show()\n",
    "\n",
    "sns.countplot(x='Sex', hue='Survived', data=df)\n",
    "plt.title('Survival by Sex')\n",
    "plt.show()\n",
    "\n",
    "sns.countplot(x='Pclass', hue='Survived', data=df)\n",
    "plt.title('Survival by Passenger Class')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
#    "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Handle missing values\n",
    "df['Age'].fillna(df['Age'].median(), inplace=True)\n",
    "df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)\n",
    "df.drop(columns=['Cabin'], inplace=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": ""
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
