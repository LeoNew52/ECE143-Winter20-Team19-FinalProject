from functions.severity_nationwide.py import get_highway_accidents_and_severity

def get_highway_and_weekday_severity_demo():
    df3=snw.get_highway_accidents_and_severity()
    ax3=sns.catplot(x="Highway", y="Severity", data=df3, color='C0',
                    height=6, kind="bar",ci=99)
    ax3.set_ylabels(rotation=0,fontsize=12)
    ax3.set_xlabels(rotation=0,fontsize=12)
