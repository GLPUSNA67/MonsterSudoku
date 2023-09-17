# def find_triple_Old():
#     for item in triple_candidate_list:
#         if item:
#         # print("716 item nums are ", item[0], item[1], item[2], item[3])
#             i_row = int(item[0])
#             i_col = int(item[1])
#             i_sq = int(item[2])
#             i_pair = item[3] # i_pair is the duple (the two numbers) being considered as a potential duple
#         try:
#             for item in triple_candidate_list:
#                 # if item[0] and item[1] and item[2] and item[3]:
#                 c_row = int(item[0])
#                 c_col = int(item[1])
#                 c_sq = int(item[2])
#                 c_pair = item[3]
#                 # If the cell to compare is the original cell, pass
#                 if i_pair == c_pair and i_row == c_row and i_col == c_col and i_sq == c_sq:
#                     pass
#                 # If the current cell is not the same as the original cell, process it
#                 elif i_pair == c_pair and (i_row == c_row or i_col == c_col or i_sq == c_sq):
#                     ex_text = f"{i_row}, {i_col}, {i_sq}, {i_pair}, {c_row}, {c_col}, {c_sq}, {c_pair}"
#                     print("741 pairs are ", i_row, i_col, i_sq, i_pair, c_row, c_col, c_sq, c_pair, c_pair[0], c_pair[1])
#                     # duple_first = {i_row}, {i_col}, {i_sq}, {i_pair}
#                     triple_first = f"{i_row}, {i_col}, {i_sq}, {i_pair}"
#                     triple_first = triple_first.split(',')
#                     triple_second = f"{c_row}, {c_col}, {c_sq}, {c_pair}"
#                     triple_second = triple_second.split(',')
#                     print("747 triple_first is ", triple_first, triple_second)
#                     print("748 triples_list is ", triple_first[0], triple_second[1])
#                     triple_candidate_list.append(list(triple_first[0], triple_second[1]))
#                     # txt_Explain.delete(0, END)
#                     txt_Explain.insert(END, ex_text)
#                     txt_Explain.insert(END, "\n")
#                     # duple_list_1 = duple_first.split(',')
#                     print("901 triple_list parts are ", triple_first, triple_first[0], triple_first[1])
#                     # duple_list_2 = duple_second.split(',')
#                     triple_candidate_list = [triple_first, triple_second]
#                     print("1062 duple_candidate_list is ", triple_candidate_list)
#                     if triple_candidate_list != []:
#                         triple_candidate_list.append(triple_candidate_list)
#                         ex_text = f"1065 triple_candidate_list is {triple_candidate_list}" 
#                         txt_Explain.insert(END, ex_text)
#                         print("1067 triples_list is ", triples_list)
#                         process_duple_list(triple_first, triple_second)

#         except Exception as e:
#             pass
#     # make_RCS_sets(4)