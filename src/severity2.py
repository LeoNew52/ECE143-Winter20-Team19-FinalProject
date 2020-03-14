from functions.severity_nationwide import get_highway_accidents_and_severity
import functions.severity_nationwide as snw
import seaborn as sns

def get_highway_and_weekday_severity_demo():
    df3=snw.get_highway_accidents_and_severity()
    ax3=sns.catplot(x="Highway", y="Severity", data=df3, color='C0',
                    height=6, kind="bar",ci=99)
    ax3.set_ylabels(rotation=0,fontsize=12)
    ax3.set_xlabels(rotation=0,fontsize=12)
    
    ax2=sns.catplot(x="Day of Week", y="Severity", data=df3, color='orange',
                    height=6, kind="bar",ci=99)
    ax2.set_ylabels(rotation=0,fontsize=20,y=1.08)
    ax2.set_xlabels(rotation=0,fontsize=20)
    ax2.set_xticklabels(rotation=30,fontsize=15)

def main():
    get_highway_and_weekday_severity_demo()

if __name__ == '__main__':
    main()
