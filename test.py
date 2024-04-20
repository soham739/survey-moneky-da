import pandas as pd

dataset = pd.read_excel("D:\\Project_da\\Data - Survey Monkey Output edited.xlsx", sheet_name="Edited_Data")

dataset_modified = dataset.copy()

columns_to_drop = ['Start Date', 'End Date', 'Email Address','First Name', 'Last Name', 'Custom Data 1']
dataset_modified = dataset_modified.drop(columns=columns_to_drop)
id_vars = list(dataset_modified.columns)[:8]
value_vars = list(dataset_modified.columns)[8:]

#Unpivoting or melting the data
'''DataFrame.melt(id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)'''

dataset_melt = dataset_modified.melt(id_vars=id_vars,value_vars=value_vars,var_name='Questions+Subquestions',value_name='Answers' )#Main dataset

# dataset_melt.to_excel("/datasetmelt.xlsx")


questions_import = pd.read_excel("D:\\Project_da\\Data - Survey Monkey Output edited.xlsx", sheet_name="Questions")
questions = questions_import.copy()

questions = questions.drop(columns=["Raw Question","Raw Subquestion","Subquestions"])#Questions dataset

questions_merged = pd.merge(left=dataset_melt,right=questions,how="left",left_on="Questions+Subquestions",right_on="Questions + Subquestions")
del questions_merged

questions = questions.rename(columns={"Questions + Subquestions":"Questions+Subquestions"})
dataset_merged = pd.merge(left=dataset_melt,right=questions,how="left",left_on="Questions+Subquestions",right_on="Questions+Subquestions")
print("merged data len:",len(dataset_merged))
print("original data len:",len(dataset_melt))
respondants = dataset_merged[dataset_merged["Answers"].notna()]
answer_dataset = respondants.groupby("Questions")["Respondent ID"].nunique().reset_index()
answer_dataset.rename(columns={"Respondent ID":"Respondants"},inplace=True)


# dataset_merged[dataset_merged["Answers"].notna()]

dataset_merged_two = pd.merge(left=dataset_merged,right=answer_dataset,how="left",left_on="Questions",right_on="Questions")
print("original data",len(dataset_merged))
print("merged data",len(dataset_merged_two))
total_answers = dataset_merged
total_answers = total_answers.groupby(["Questions+Subquestions","Answers"])["Respondent ID"].nunique().reset_index()
total_answers.rename(columns={"Respondent ID":"Same Answer"},inplace=True)
dataset_merged_three = pd.merge(left=dataset_merged_two,right=total_answers,how="left",left_on=["Questions+Subquestions","Answers"],right_on=["Questions+Subquestions","Answers"])

print("original data",len(dataset_merged_two))
print("merged data",len(dataset_merged_three))
dataset_merged_three = pd.merge(left=dataset_merged_two,right=total_answers,how="left",left_on=["Questions+Subquestions","Answers"],right_on=["Questions+Subquestions","Answers"])

print("original data",len(dataset_merged_two))
print("merged data",len(dataset_merged_three))
dataset_merged_three = pd.merge(left=dataset_merged_two,right=total_answers,how="left",left_on=["Questions+Subquestions","Answers"],right_on=["Questions+Subquestions","Answers"])
print("original data",len(dataset_merged_two))
print("merged data",len(dataset_merged_three))
dataset_merged_three = pd.merge(left=dataset_merged_two,right=total_answers,how="left",left_on=["Questions+Subquestions","Answers"],right_on=["Questions+Subquestions","Answers"])
dataset_merged_three['Same Answer'].fillna(0, inplace=True)
print("original data",len(dataset_merged_two))
print("merged data",len(dataset_merged_three))
output = dataset_merged_three.copy()

#Renaming the columns
output = output.rename(columns={'Identify which division you work in.-Response':'Division Primary','Identify which division you work in.-Other (please specify)':'Division Secondary','Which of the following best describes your position level?-Response':'Position','Which generation are you apart of?-Response':'Generation','Please select the gender in which you identify.-Response':'Gender','Which duration range best aligns with your tenure at your company?-Response':'Tenure','Which of the following best describes your employment type?-Response':'Employment Type'})
output.to_excel("D:\\Project_da\\Final_Output_Sheet.xlsx",index=False)   #Final data export


