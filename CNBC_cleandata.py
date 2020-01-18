#############################################
# Merge all info together
# Count each video's guest(s) and host(s)
# Find if there is third party
# Modify CEO and Company name to be uniform
# Count numbers of CEOs, Companies and Hosts
#############################################

import pandas as pd
import re
from difflib import SequenceMatcher


def read_in_file(path, info_path):
    frame_path = info_path
    path1 = ('/').join(path.split('/')[:-1]) + '/'
    df = pd.read_csv(path)         # df contains raw data
    df3 = pd.read_csv(frame_path)  # df3 contains extra info include number of frames, width, length, duration

    df = count_hosts_guests(df)    # count number of hosts and number of ceo. two new columns, each row will show number of hosts and ceo in each show

    df = merge_frame(df3,df)       # merge extra info with raw data

    df = change_Tparty(df)         # generate a column to show if there is third party


    df['CEO_origin'] = df['CEO']
    df['Company_origin'] = df['Company']
    df['Interviewer_origin'] = df['Interviewer']
    df = clean_extra_content(df, ['Interviewer', 'CEO', 'Company'])
    df2 = df.copy()

    df = find_similar(df2, 'Company', 'CEO', df)          # change company name if they have same ceo and their names are similar
    df = find_similar(df2, 'CEO', 'Company',  df)         # change ceo name if they have same company name and their names are similar
    path3 = path.replace('data', 'final_output')
    df = df.drop_duplicates(subset = 'video_id',keep = 'first', inplace = False)
    df.to_csv(path3)
    print("### Output has been generated to " + path3 + " ###\n")

    hosts_num, ceo_num, comp_numb = count_result(df, path1)            # count the total number of hosts, CEOs and companies
    print("Number of Host: %s, Number of CEO: %s, Number of Company: %s, Nunmber of Video: %s \n" % (hosts_num, ceo_num, comp_numb, len(df.index)))


def count_hosts_guests(df):
    for i,r in df.iterrows():
        if type(r['Interviewer']) != float:
            hosts_count = r['Interviewer'].count('/')
            df.at[i, 'hosts_count'] = hosts_count + 1
        else:
            df.at[i, 'hosts_count'] = 0
        if type(r['CEO']) != float:
            hosts_count = r['CEO'].count('/')
            df.at[i, 'CEO_count'] = hosts_count + 1
        else:
            df.at[i, 'CEO_count'] = 0
    return df


def count_result(df2, path):
    hosts_set = find_all(df2, 'Interviewer')
    company_set = find_all(df2, 'Company')
    ceo_set = find_all(df2, 'CEO')
    save_csv(hosts_set, path, 'Host', 'Hostscount')
    save_csv(company_set, path, 'Company', 'Companyscount')
    save_csv(ceo_set, path, 'CEO', 'CEOscount')
    return len(hosts_set),len(ceo_set),len(company_set)


def clean_extra_content(df2,col_list):
    for each_col in col_list:
        for i, r in df2.iterrows():
            if type(r[each_col]) != float:
                if '(' in r[each_col]:
                    text = re.findall(r'\(.*?\)', r[each_col])
                    for each_text in text:
                        update_text = r[each_col].replace(each_text, '').title().strip()
                        df2.at[i, each_col] = update_text
                else:
                    df2.at[i, each_col] = r[each_col].title().strip()
    return df2


def find_all(df,col):
    dic = {}
    for i,r in df.iterrows():
        if (type(r[col]) != float) &(r[col] != 'NA'):
            list_hosts = r[col].split('/')
            for each_host in list_hosts:
                each_host = each_host.strip()
                if each_host in dic:
                    dic[each_host] +=1
                else:
                    dic[each_host] = 1
    for each_key in dic.keys():
        if len(each_key)<2:
            dic.pop(each_key)
            break
    return dic


def save_csv(Set, path, column1,column2):
    dfObj = pd.DataFrame.from_dict(Set, orient='index')
    dfObj = dfObj.reset_index()
    col = [column1, column2]
    dfObj.columns = col
    name = path +column2+'.csv'
    dfObj.to_csv(name)
    print("### %s detail has been generated to %s ###\n" % (column2, name))


def merge_frame(df3,df):
    df3['video_id'] = df3['video_id'].astype(int)
    df = df.merge(df3, on= 'video_id', how = 'left')
    df = df.drop(columns=['Unnamed: 0_x', 'Unnamed: 0_y', 'Show'])
    return df


def change_Tparty(df):
    for i,r in df.iterrows():
        if type(r['Interviewer']) != float:
            if '/' in r['Interviewer']:
                df.at[i, 'Tparty'] = 'Y'
            else:
                df.at[i, 'Tparty'] = 'N'
        if type(r['CEO']) != float:
            if ('/' in r['CEO']):
                df.at[i, 'Tparty'] = 'Y'
    for i,r in df.iterrows():
        if type(r['Tparty']) == float:
            df.at[i, 'Tparty'] = 'N'
    return df


##################################################
# first time is same ceo name, diff company name
# second time is same company, diff ceo name
# replace the content in df by comparing df2
# if the similarity between two records arr bigger
# than 0.6 which mean they are more than half
# different, it will be replace by the previous
# one
# if there were more than 2 records, they will be
# compared with each other and find the combination
# which is more than 0.6 and modify the specific
# one.
# if all of them are below 0.6, no modify.
# if more than 3 records, do not support
##################################################
def find_similar(df2, col, col1,df):
    dic = find_all(df2,col1)
    for key, value in dic.items():
        df_part = df2[(df2[col1] == key) & (df2[col].str.contains('/') == False)]
        df_part1 = df_part.drop_duplicates(subset = col,keep = 'first', inplace = False)
        if (len(df_part1) ==2):
            seq_ratio = SequenceMatcher(None, df_part1.at[df_part1.index[0],col], df_part1.at[df_part1.index[1],col]).ratio()
            if seq_ratio> 0.6:
                for i in df_part.index:
                    df.at[i, col] = df.at[df_part.index[0], col]
        if (len(df_part1) ==3):
            ratio_12 = SequenceMatcher(None, df_part1.at[df_part1.index[0],col], df_part1.at[df_part1.index[1],col]).ratio()
            ratio_13 = SequenceMatcher(None, df_part1.at[df_part1.index[0],col], df_part1.at[df_part1.index[2],col]).ratio()
            ratio_23 = SequenceMatcher(None, df_part1.at[df_part1.index[1],col], df_part1.at[df_part1.index[2],col]).ratio()
            list_ratio =[ratio_12,ratio_13,ratio_23]
            if all(i >= 0.6 for i in list_ratio):
                for i in df_part.index:
                    df.at[i, col] = df.at[df_part.index[0], col]
            elif all(i <= 0.6 for i in list_ratio):
                pass
            else:
                max_ratio = max(list_ratio)
                if ratio_12 == max_ratio:
                    df_part= df_part[df_part[col] == df_part1.at[df_part1.index[1],col]]
                    for i in df_part.index:
                        df.at[i, col] = df.at[df_part1.index[0], col]
                elif ratio_23 == max_ratio:
                    df_part = df_part[df_part[col] == df_part1.at[df_part1.index[2], col]]
                    for i in df_part.index:
                        df.at[i, col] = df.at[df_part1.index[1], col]
                else:
                    df_part = df_part[df_part[col] == df_part1.at[df_part1.index[2], col]]
                    for i in df_part.index:
                        df.at[i, col] = df.at[df_part1.index[0], col]
        if len(df_part1) >3:
            print('Too many contents')
            break

    return df


path = 'csv file after collect all manually collected info'
info_path = 'csv file after using ffmpeg'
read_in_file(path, info_path)

