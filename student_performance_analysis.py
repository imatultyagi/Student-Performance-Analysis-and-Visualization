import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Load CSV File
df = pd.read_csv("students.csv")

print(df.head())

# =====================================================
# Question 2
# How can total and average marks
# be calculated automatically?
# =====================================================

df['Total'] = df[
    ['Math', 'Science', 'English']].sum(axis=1)

df['Average'] = df['Total'] / 3

print("\nTotal and Average:\n")

print(df[['Student', 'Total', 'Average']])

# =====================================================
# Question 3
# How can grades be assigned automatically?
# =====================================================

def grade(avg):

    if avg >= 85:
        return 'A'

    elif avg >= 70:
        return 'B'

    else:
        return 'C'

df['Grade'] = df['Average'].apply(grade)

print("\nGrades:\n")

print(df[['Student', 'Grade']])

# =====================================================
# Question 4
# How can topper and rankings
# be identified automatically?
# =====================================================

topper = df.loc[
    df['Total'].idxmax(),
    'Student'
]

df['Rank'] = df['Total'].rank(
    ascending=False
).astype(int)

print("\nUpdated Data:\n")

print(df)

print("\nTopper:", topper)

# =====================================================
# Question 5
# How can top-performing students
# be compared using bar chart?
# =====================================================

top7 = df.sort_values(
    by='Total',
    ascending=False
).head(7)

plt.figure(figsize=(14, 7))

colors = []

for student, grade_val in zip(
    top7['Student'],
    top7['Grade']
):

    if student == topper:
        colors.append('blue')

    elif grade_val == 'A':
        colors.append('green')

    elif grade_val == 'B':
        colors.append('orange')

    else:
        colors.append('red')

bars = plt.bar(
    top7['Student'],
    top7['Total'],
    color=colors,
    edgecolor='black'
)

# Add values and ranks
for bar, rank in zip(
    bars,
    top7['Rank']
):

    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 2,
        f'{int(height)}\n(Rank {rank})',
        ha='center',
        fontsize=8,
        fontweight='bold'
    )

# Legend
legend_labels = [

    mpatches.Patch(
        color='blue',
        label='Topper'
    ),

    mpatches.Patch(
        color='green',
        label='Grade A'
    ),

    mpatches.Patch(
        color='orange',
        label='Grade B'
    ),

    mpatches.Patch(
        color='red',
        label='Grade C'
    )
]

plt.legend(handles=legend_labels)

plt.title(
    "Top 7 Student Performance Analysis",
    fontsize=14,
    fontweight='bold'
)

plt.xlabel("Students")
plt.ylabel("Total Marks")

plt.xticks(rotation=25)

plt.grid(
    axis='y',
    linestyle='--',
    alpha=0.6
)

plt.tight_layout()

plt.savefig("bar_chart.png")

plt.show()

# =====================================================
# Question 6
# How can subject-wise performance trends
# be analyzed using line chart?
# =====================================================

plt.figure(figsize=(14, 7))

for subject in [
    'Math',
    'Science',
    'English'
]:

    plt.plot(
        top7['Student'],
        top7[subject],
        marker='o',
        linewidth=2,
        label=subject
    )

# Add value labels
for subject in [
    'Math',
    'Science',
    'English'
]:

    for i, value in enumerate(top7[subject]):

        plt.text(
            i,
            value + 1,
            str(value),
            ha='center',
            fontsize=8
        )

plt.title(
    "Subject-wise Performance of Top 7 Students",
    fontsize=14,
    fontweight='bold'
)

plt.xlabel("Students")
plt.ylabel("Marks")

plt.xticks(rotation=25)

plt.legend()

plt.grid(
    True,
    linestyle='--',
    alpha=0.6
)

plt.tight_layout()

plt.savefig("line_chart.png")

plt.show()

# =====================================================
# Question 7
# How can overall grade distribution
# be represented using pie chart?
# =====================================================

plt.figure(figsize=(8, 8))

grade_counts = df['Grade'].value_counts()

colors = [
    'green',
    'orange',
    'red'
]

explode = [0.05] * len(grade_counts)

plt.pie(
    grade_counts,

    labels=grade_counts.index, # pyright: ignore[reportArgumentType]

    autopct='%1.1f%%',

    colors=colors,

    explode=explode,

    shadow=True,

    startangle=140
)

plt.title(
    "Overall Grade Distribution",
    fontsize=14,
    fontweight='bold'
)

plt.tight_layout()

plt.savefig("pie_chart.png")

plt.show()

# =====================================================
# Question 8
# How can relationship between Math and Science
# marks be analyzed using scatter plot?
# =====================================================
import matplotlib.pyplot as plt

grade_colors = {
    'A': 'green',
    'B': 'orange',
    'C': 'red'
}

colors = [
    grade_colors[g]
    for g in df['Grade']
]

plt.figure(figsize=(12,8))

plt.scatter(
    df['Math'],
    df['Science'],
    c=colors,
    s=70,
    alpha=0.7,
    edgecolors='black'
)

plt.title("Math vs Science Performance by Grade")
plt.xlabel("Math Marks")
plt.ylabel("Science Marks")

plt.grid(True)

plt.show()

# =====================================================
# Question 9
# How can marks distribution
# be analyzed using histogram?
# =====================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df['Total'],
    bins=8,
    color='skyblue',
    edgecolor='black'
)

plt.title(
    "Distribution of Total Marks",
    fontsize=14,
    fontweight='bold'
)

plt.xlabel("Total Marks")
plt.ylabel("Number of Students")

plt.grid(
    linestyle='--',
    alpha=0.6
)

plt.tight_layout()

plt.savefig("histogram.png")

plt.show()

# =====================================================
# Question 10
# How can subject averages be compared
# using horizontal bar chart?
# =====================================================

subject_avg = [

    df['Math'].mean(),

    df['Science'].mean(),

    df['English'].mean()
]

subjects = [
    'Math',
    'Science',
    'English'
]

plt.figure(figsize=(10, 5))

plt.barh(
    subjects,
    subject_avg,
    color=['red', 'green', 'blue']
)

plt.title(
    "Average Marks by Subject",
    fontsize=14,
    fontweight='bold'
)

plt.xlabel("Average Marks")
plt.ylabel("Subjects")

plt.grid(
    axis='x',
    linestyle='--',
    alpha=0.6
)

plt.tight_layout()

plt.savefig("horizontal_bar_chart.png")

plt.show()

# =====================================================
# Question 11
# How can subject performance trends
# be analyzed using area chart?
# =====================================================

plt.figure(figsize=(14, 7))

plt.stackplot(

    top7['Student'],

    top7['Math'],
    top7['Science'],
    top7['English'],

    labels=['Math', 'Science', 'English'],

    alpha=0.8
)

plt.title(
    "Subject-wise Area Chart Analysis",
    fontsize=14,
    fontweight='bold'
)

plt.xlabel("Students")
plt.ylabel("Marks")

plt.xticks(rotation=25)

plt.legend(loc='upper left')

plt.tight_layout()

plt.savefig("area_chart.png")

plt.show()

# =====================================================
# Question 12
# How can correlation between subjects
# be identified?
# =====================================================

correlation = df[
    ['Math', 'Science', 'English']
].corr()

print("\nCorrelation Matrix:\n")

print(correlation)

# =====================================================
# Question 13
# How can overall class performance
# statistics be summarized?
# =====================================================

print(
    "\nClass Total Marks:",
    df['Total'].sum()
)

print(
    "Class Average Marks:",
    round(df['Average'].mean(), 2)
)