# %%
# data links:
# https://data.world/vizzup/mental-health-depression-disorder-data/workspace/file?filename=Mental+health+Depression+disorder+Data.xlsx
# https://www.statista.com/statistics/184272/educational-attainment-of-college-diploma-or-higher-by-gender/


# %%
import pandas as pd
import altair as alt
import datadotworld as dw

# 25 years and older
college_grad_data = pd.read_csv('taba-2.csv')


# %%
total_college_grad_data = college_grad_data.filter(["Year", "Total"])
total_college_grad_data


# %%
college_grad_chart = (alt.Chart(college_grad_data, title="College Grads Over 25")
                        .mark_line()
                        .encode(
                            x = 'Year',
                            y = alt.Y('Total', title="Total %")
                        )
                        .interactive()
)
college_grad_chart


# %%
female_college_grad_data = college_grad_data.filter(["Year", "Female"])
female_college_grad_data


# %%
female_college_grad_chart = (alt.Chart(college_grad_data, title="College Grads Over 25")
                        .mark_line(
                            color='red'
                        )
                        .encode(
                            x = 'Year',
                            y = alt.Y('Female', title="Female %")
                        )
                        .interactive()
)
female_college_grad_chart


# %%
male_college_grad_data = college_grad_data.filter(["Year", "Male"])
male_college_grad_data


# %%
male_college_grad_chart = (alt.Chart(college_grad_data, title="College Grads Over 25")
                        .mark_line(
                            color='green'
                        )
                        .encode(
                            x = 'Year',
                            y = alt.Y('Male', title="Male %")
                        )
                        .interactive()
)
male_college_grad_chart


# %%
final_chart = male_college_grad_chart + female_college_grad_chart + college_grad_chart
final_chart


# %%
mental_health_data_total = dw.query('vizzup/mental-health-depression-disorder-data', 
                                    '''SELECT code, year, (bipolar_disorder + eating_disorders + anxiety_disorders + depression) as total_mental_health 
                                    FROM prevalence_by_mental_and_substa 
                                    WHERE code = "USA" 
                                    ORDER BY total_mental_health DESC''')

print(mental_health_data_total.dataframe)


# %%
mental_health_chart = (alt.Chart(mental_health_data_total.dataframe, name= "Mental Health Over Past 20 Years")
                          .mark_line()
                          .encode(
                              x = alt.X('year'),
                              y = alt.Y('total_mental_health')
                          )
                          .interactive()                     
)
mental_health_chart


# %%
mental_health_vs_college_grad = college_grad_chart + mental_health_chart
mental_health_vs_college_grad

# %% [markdown]
# From the above graph I learned that mental health diagnosis over the last 20 years have actually remained almost entirely consistent. In the inverse more people have been graduating from college. There does not appear to be any correlation between college graduation rates and an increase in mental health diagnosis.
# %% [markdown]
# # Mental Health by Country Analysis

# %%
top_10_bipolar = dw.query('vizzup/mental-health-depression-disorder-data', 
                                    '''SELECT code, AVG(bipolar_disorder) AS bipolar, AVG(eating_disorders) AS eating_disorders, AVG(anxiety_disorders) AS anxiety, AVG(depression) AS depression 
                                    FROM prevalence_by_mental_and_substa 
                                    GROUP BY code
                                    ORDER BY bipolar DESC
                                    LIMIT 10
                                    ''')
top_10_bipolar.dataframe


# %%
worst_bipolar_chart = (alt.Chart(top_10_bipolar.dataframe, title="Avg. Prevelance of Bipolar by Country")
                               .mark_bar()
                               .encode(
                                   x = alt.X('code', title="Country"),
                                   y = alt.Y('bipolar', title="Bipolar % of Population"),
                                   color = 'code'
                               )
)
worst_bipolar_chart


# %%
top_10_eating_disorder = dw.query('vizzup/mental-health-depression-disorder-data', 
                                    '''SELECT code, AVG(bipolar_disorder) AS bipolar, AVG(eating_disorders) AS eating_disorders, AVG(anxiety_disorders) AS anxiety, AVG(depression) AS depression 
                                    FROM prevalence_by_mental_and_substa 
                                    GROUP BY code
                                    ORDER BY eating_disorders DESC
                                    LIMIT 10
                                    ''')
top_10_eating_disorder.dataframe


# %%
worst_eating_chart = (alt.Chart(top_10_eating_disorder.dataframe, title="Avg. Prevelance of Eating Disorder by Country")
                               .mark_bar()
                               .encode(
                                   x = alt.X('code', title="Country"),
                                   y = alt.Y('eating_disorders', title="Eating Disorders % of Population"),
                                   color = 'code'
                               )
)
worst_eating_chart


# %%
top_10_anxiety = dw.query('vizzup/mental-health-depression-disorder-data', 
                                    '''SELECT code, AVG(bipolar_disorder) AS bipolar, AVG(eating_disorders) AS eating_disorders, AVG(anxiety_disorders) AS anxiety, AVG(depression) AS depression 
                                    FROM prevalence_by_mental_and_substa 
                                    GROUP BY code
                                    ORDER BY anxiety DESC
                                    LIMIT 10
                                    ''')
top_10_anxiety.dataframe


# %%
worst_anxiety = (alt.Chart(top_10_anxiety.dataframe, title="Avg. Prevelance of Anxiety by Country")
                               .mark_bar()
                               .encode(
                                   x = alt.X('code', title="Country"),
                                   y = alt.Y('anxiety', title="Anxiety % of Population"),
                                   color = 'code'
                               )
)
worst_anxiety


# %%
top_10_depression = dw.query('vizzup/mental-health-depression-disorder-data', 
                                    '''SELECT code, AVG(bipolar_disorder) AS bipolar, AVG(eating_disorders) AS eating_disorders, AVG(anxiety_disorders) AS anxiety, AVG(depression) AS depression 
                                    FROM prevalence_by_mental_and_substa 
                                    GROUP BY code
                                    ORDER BY depression DESC
                                    LIMIT 10
                                    ''')
top_10_depression.dataframe


# %%
worst_depression = (alt.Chart(top_10_depression.dataframe, title="Avg. Prevelance of Depression by Country")
                               .mark_bar()
                               .encode(
                                   x = alt.X('code', title="Country"),
                                   y = alt.Y('depression', title="Depression % of Population"),
                                   color = 'code'
                               )
)
worst_depression
# greenland has the worst...followed by Morroco (North Africa)


