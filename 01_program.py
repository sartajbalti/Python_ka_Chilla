from tkinter.ttk import Style
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(Style="ticks", color_code=True)

titanic = sns.load_dataset("titanic")
print(titanic)
# p = sns.countplot(x="", y="", data= titanic)
# plt.show()