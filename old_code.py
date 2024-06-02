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
# p_dict[s_dict]['formula'] = eci_1
# print("809 ", s_dict, s_type, eci_1)
# print("810 ", s_dict, s_type, eci_1, s_1_dict['formula'])

# print(s_1_dict['type'])
# eci_1 = cb_eci_1.get()
# s_1_dict['formula'] = eci_1
# s_dict = s_1_dict['id']


# def set_eci_2_obsolete(eventObject):
#     e_Explanation.insert(tk.END, "716 function set_eci_2 entered\n")
#     print("717 function set_eci_2 entered\n")
#     s_2_type = s_2_dict['type']
#     print("725 s_2_type is ", s_2_type, s_2_dict['type'])
#     eci_2 = cb_eci_2.get()
#     s_2_dict['formula'] = eci_2
#     s_dict = s_2_dict['id']
#     print("722 go to setSelectedItemName(s_dict, s_type, s_id_formula)", s_2_type, eci_2)
#     if s_2_dict['type'] == 'element':
#         print("730 s_2_dict['type'] is ")
#         setSelectedItemName('s_2_dict', s_2_type, eci_2)
#     elif s_2_dict['type'] == 'compound':
#         setSelectedItemName('s_2_dict', s_2_type, eci_2)
#     elif s_2_dict['type'] == 'ion':
#         setSelectedItemName('s_2_dict', s_2_type, eci_2)
#     elif s_2_dict['type'] == 'diatomic':
#         setSelectedItemName('s_2_dict', s_2_type, eci_2)
# if s_id_formula in c_dict:
#     c_dict[s_id_formula]

# substance = c_db[s_id_formula]
# name = c_db[s_id_formula]
# print("1062 ", substance)
# res = list(c_dict.keys()).index(s_id_formula)
# print("Index of search key is : " + str(res))
# print("1063", AlCl3['mass'])
# print("1064", BCl3['mass'])
# # print("1064", s_id_formula['mass']) # doesn't work
# print("1065", c_dict[s_id_formula])
# # print("1065", c_dict[s_id_formula][res])
# print("1076", desn[s_id_formula])
# print("1077", desm[s_id_formula])
# print('1078 compound found!', s_id_formula, s_id_formula[0], s_id_formula[1]) # doesn't work

# print('1060 compound found!', s_id_formula['name'], s_id_formula['mass']) # doesn't work
# else:
#     print("1062 compound not found")
# don't print s_dict, it is not s_x_dict, it is the whole dict
# name = c_db[s_id_formula]
# print("953 ", desn[s_id_formula]) # [s_id_formula]['Al4C3']
# print("953 ", name)
# name = p_dict[s_1_dict]['name']
# cb_eci_1_N.set(name)
# # eci_1_name = p_dict[eci_1]['name']
# # eci_1_mass = p_dict[eci_1]['mass']
# print("850 p_dict[eci_1]['name'] is ", p_dict[eci_1]['name'])
# print("851 p_dict[eci_1]['mass'] is ", p_dict[eci_1]['mass'])

# e_eci_1_qty.delete(0, END)
# e_eci_1_qty.insert(0, mass)
# cb_eci_1_units.set('grams')

# e_eci_1_M_qty.delete(0, END)
# e_eci_1_M_qty.insert(0, 1.0)

# print("833 ", s_1_dict)
# cb_eci_1_N['values'] = s_1_dict['formula']
# cb_eci_1_N = s_1_dict['formula']
# print("829 db[eci_1]['name'] is ", db[eci_1]['name'])
# do not work: p_dict[s_dict]['name'], p_dict[s_1_dict]['name'], p_dict['s_1_dict']['name']
# print("859 p_dict[eci_1]['mass'] is ", p_dict['s_1_dict']['mass'])
# print("860 p_dict[eci_1]['densitydensity'] is ", p_dict['s_1_dict']['density'])
# print("851 s_dict ", s_dict)
# print("852 p_dict ", p_dict[0])
# print("842 p_dict[s_1_dict]['name'] ", p_dict[s_1_dict]['name'])
# name = p_dict[s_dict]['name']
# mass = p_dict[s_dict]['mass']
# db[eci_1]['name'] = db[s_id_formula]['name']
# p_dict[s_1_dict]['name'] = db[s_id_formula]['name']
# p_dict[s_1_dict]['mass'] = db[s_id_formula]['mass']

# symbol = s_1_dict['formula']
# print("798 symbol", symbol)
# print("798 in set_eci_1", s_dict['formula'])
# if s_1_dict['type'] == 'element':
#     print("793", s_1_dict['type'])
#     set_eci_formula('s_1_dict', s_1_dict['type'], formula)
# elif s_1_dict['type'] == 'compound':
#     print("795", s_1_dict['type'])
#     set_eci_formula('s_1_dict', s_1_dict['type'], formula)
# elif s_1_dict['type'] == 'ion':
#     print("797", s_1_dict['type'])
#     set_eci_formula('s_1_dict', s_1_dict['type'], formula)
# elif s_1_dict['type'] == 'diatomic':
#     print("799", s_1_dict['type'])
#     set_eci_formula('s_1_dict', s_1_dict['type'], formula)
#   s_dict = 's_1_dict'
#   mass = s_1_dict["mass"]

#   refresh_S_1()
#   print("890", s_1_dict["qty"])
# def set_eci_3(eventObject):
#     e_Explanation.insert(tk.END, "733 function set_eci_3 entered\n")
#     print("734 function set_eci_3 entered\n")
#     s_3_type = s_3_dict['type']
#     eci_3 = cb_eci_3.get()
#     s_3_dict['formula'] = eci_3
#     s_dict = s_3_dict['id']
#     if s_3_dict['type'] == 'element':
#         setSelectedItemName('s_3_dict', s_3_type, eci_3)
#     elif s_3_dict['type'] == 'compound':
#         setSelectedItemName('s_3_dict', s_3_type, eci_3)
#     elif s_3_dict['type'] == 'ion':
#         setSelectedItemName('s_3_dict', s_3_type, eci_3)
#     elif s_3_dict['type'] == 'diatomic':
#         setSelectedItemName('s_3_dict', s_3_type, eci_3)


# def set_eci_4(eventObject):
#     e_Explanation.insert(tk.END, "749 function set_eci_4 entered\n")
#     print("750 function set_eci_4 entered\n")
#     s_4_type = s_4_dict['type']
#     eci_4 = cb_eci_4.get()
#     s_4_dict['formula'] = eci_4
#     s_dict = s_4_dict['id']
#     if s_4_dict['type'] == 'element':
#         setSelectedItemName('s_4_dict', s_4_type, eci_4)
#     elif s_4_dict['type'] == 'compound':
#         setSelectedItemName('s_4_dict', s_4_type, eci_4)
#     elif s_4_dict['type'] == 'ion':
#         setSelectedItemName('s_4_dict', s_4_type, eci_4)
#     elif s_4_dict['type'] == 'diatomic':
#         setSelectedItemName('s_4_dict', s_4_type, eci_4)


# def set_eci_5(eventObject):
#     e_Explanation.insert(tk.END, "797 function set_eci_5 entered\n")
#     print("798 function set_eci_5 entered\n")
#     s_5_type = s_5_dict['type']
#     eci_5 = cb_eci_5.get()
#     s_5_dict['formula'] = eci_5
#     s_dict = s_5_dict['id']
#     if s_5_dict['type'] == 'element':
#         setSelectedItemName('s_5_dict', s_5_type, eci_5)
#     elif s_5_dict['type'] == 'compound':
#         setSelectedItemName('s_5_dict', s_5_type, eci_5)
#     elif s_5_dict['type'] == 'ion':
#         setSelectedItemName('s_5_dict', s_5_type, eci_5)
#     elif s_5_dict['type'] == 'diatomic':
#         setSelectedItemName('s_5_dict', s_5_type, eci_5)


# def set_eci_6(eventObject):
#     e_Explanation.insert(tk.END, "812 function set_eci_6 entered\n")
#     print("813 function set_eci_6 entered\n")
#     s_6_type = s_6_dict['type']
#     eci_6 = cb_eci_6.get()
#     s_6_dict['formula'] = eci_6
#     s_dict = s_6_dict['id']
#     if s_6_dict['type'] == 'element':
#         setSelectedItemName('s_6_dict', s_6_type, eci_6)
#     elif s_6_dict['type'] == 'compound':
#         setSelectedItemName('s_6_dict', s_6_type, eci_6)
#     elif s_6_dict['type'] == 'ion':
#         setSelectedItemName('s_6_dict', s_6_type, eci_6)
#     elif s_6_dict['type'] == 'diatomic':
#         setSelectedItemName('s_6_dict', s_6_type, eci_6)
# refresh_S_1(s_x_dict)
# print("903  ", mass,)
# print("904  ", inputValue,)
# s_dict["M_qty"] = float(inputValue)/float(mass)
# print("906  ", mass, s_dict["M_qty"])

# def set_e_eci_2_M_qty(eventObject):
#     print("854 Entered set_e_eci_2_M_qty")
#     M_qty = e_eci_2_M_qty.get()
#     s_2_dict["M_qty"] = M_qty
#     print("857", M_qty)
#     mole_mass_change(M_qty, 's_2_dict')


# def set_e_eci_3_M_qty(eventObject):
#     qty = e_eci_3_M_qty.get()
#     print("821", qty)


# def set_eci_4_qty(eventObject):
#     qty = e_eci_4_qty.get()
#     s_4_dict["qty"] = qty
#     print("848", s_4_dict["qty"])
#     mass_mole_change(qty, 's_4_dict')

# def set_eci_4_M_qty():
#     M_qty = e_eci_4_M_qty.get()


# def set_eci_5_qty(eventObject):
#     qty = e_eci_5_qty.get()
#     s_5_dict["qty"] = qty
#     print("848", s_5_dict["qty"])
#     mass_mole_change(qty, 's_5_dict')


# def set_e_eci_5_M_qty(eventObject):
#     qty = e_eci_5_M_qty.get()
#     print("821", qty)


# def set_eci_6_qty(eventObject):
#     qty = e_eci_6_qty.get()
#     s_6_dict["qty"] = qty
#     print("848", s_6_dict["qty"])
#     mass_mole_change(qty, 's_6_dict')


# def set_e_eci_6_M_qty(eventObject):
#     qty = e_eci_6_M_qty.get()
#     print("821", qty)

// *****
/*
    set_initial_values(s_1_dict)

    set_substance_type('s_4_type', 's_4_dict');
    //await set_delay();
    type_select = document.getElementById('s_4_type');
    type_select.value = "compound";

    fill_substance_formulas('s_4_type', 'compound', 's_4_dict')

    //await set_delay();
    set_substance_type('s_4_type', 's_4_dict');
    //await set_delay();
    document.getElementById('substance_4_compound').focus();
    document.getElementById('substance_4_compound').blur();
    document.getElementById('substance_4_compound').value = 'Ch4';
    comF = document.getElementById('substance_4_compound');
    comF.value = 'Ch4';
    setSelectedItemName('s_4_type', 'substance_4_name_compound', 'substance_4_compound', 'Ch4')
    console.log("3483 s_4_dict", s_4_dict)
    refresh_display('s_4_dict')


# // set_substance_type('s_1_type', 's_1_dict');
# // await set_delay();
# // let type_select = document.getElementById('s_1_type');
# // type_select.value = "compound";
# // fill_substance_formulas('s_1_type', 'compound', 's_1_dict')
# // set_substance_type('s_1_type', 's_1_dict');
# // document.getElementById('substance_1_compound').focus();
# // document.getElementById('substance_1_compound').blur();
# // document.getElementById('substance_1_compound').value = 'Ch4';
# // setSelectedItemName('s_1_type', 'substance_1_name_compound', 'substance_1_compound', 'Ch4')
# // console.log("3089 s_1_dict", s_1_dict)
# // refresh_display('s_1_dict')

# // set_substance_type('s_2_type', 's_2_dict');
# // await set_delay();
# // type_select = document.getElementById('s_2_type');
# // type_select.value = "compound";
# // fill_substance_formulas('s_2_type', 'compound', 's_2_dict')
# // set_substance_type('s_2_type', 's_2_dict');
# // document.getElementById('substance_2_compound').focus();
# // document.getElementById('substance_2_compound').blur();
# // document.getElementById('substance_2_compound').value = 'Ch4';
# // setSelectedItemName('s_2_type', 'substance_2_name_compound', 'substance_2_compound', 'Ch4')
# // console.log("3089 s_2_dict", s_2_dict)
# // refresh_display('s_2_dict')
gen_dict = {

    record_id: "", environment: "", major_process: "", minor_process: "", process_yield: "", equipment: [], energy_type: "",
    energy_amount: 0, catalyst: "", side_effects: [], by_products: [], variable_list: [], values: 0, notes: ""
*/
  // Change the Substance 1 mole qty to 2
  // e = ""
  // input_qty_change(e, 's_1_qty', 's_1_dict')
  // console.log("3318 call input_qty_change(e, 's_1_qty', 's_1_dict')", 's_1_qty', 's_1_dict' )
  /*await set_delay();
    
    document.getElementById('s_1_m_qty').value = 2;
    // Hide the information panel
    await set_delay();
    handleHideShowInstructionPanel();
    // Show the information panel
    await set_delay();
    handleHideShowInstructionPanel();
    // Hide the information panel
    await set_delay();
    handleHideShowInstructionPanel();

    // Additional functions I will try to develop while on vacation.
    // Change the main qty to 7
    await set_delay();
    document.getElementById('s_1_qty').value = 7;

    // Change the mole qty to 1
    await set_delay();
    document.getElementById('s_1_m_qty').value = 1;

    // Change press units to "torr"
    await set_delay();
    document.getElementById('s_1_press_units').value = 'torr';

    // Change main units to liters
    await set_delay();
    document.getElementById('s_1_units').value = 'liters(g)';

    // Change press qty to 760
    await set_delay();
    document.getElementById('s_1_press_qty').value = 760;

    // Change main units to grams
    await set_delay();
    document.getElementById('s_1_units').value = 'grams';

    // Change main units to liters
    await set_delay();
    document.getElementById('s_1_units').value = 'liters(g)';

    // Change temp qty to 25
    await set_delay();
    document.getElementById('s_1_temp_qty').value = 25;

    // Change temp qty to 0
    await set_delay();
    document.getElementById('s_1_temp_qty').value = 0;

    // Change temp units to F
    await set_delay();
    document.getElementById('s_1_temp_units').value = 'F';

    // Change temp units to C
    await set_delay();
    document.getElementById('s_1_temp_units').value = 'C';

    // Change the mole qty to .25
    await set_delay();
    document.getElementById('s_1_m_qty').value = 0.25;

    // Change s_1_kl_qty to .5
    await set_delay();
    document.getElementById('s_1_kl_qty').value = 0.5;

    // Change s_1_kl_units to liters(l)
    await set_delay();
    document.getElementById('s_1_kl_units').value = 'liters(l)';

    // Select the minor_process "molarity or moles to liters"
    await set_delay();
    document.getElementById('select_minor_process').value = 'molarity or moles to liters';

    // Change the mole qty to .5
    await set_delay();
    document.getElementById('s_1_m_qty').value = 0.5;

    // Select the minor_process "Parse compound to ions"
    await set_delay();
    document.getElementById('select_minor_process').value = 'Parse Compound to Ions';
    
    // // Set Substance 1 type to compound
    // await set_delay();
    // type_select.value = "compound";

    // Set the Substance 1 substance to "CH4"
    await set_delay();
    let autocomplete_elements = document.getElementsByClassName('xdsoft_autocomplete');
    for (let i = 0; i < autocomplete_elements.length; i++) {
        let element = autocomplete_elements[i];
        element.classList.add('d-none');
    }
    document.getElementById('substance_1_element').classList.add('d-none');
    document.getElementById('substance_1_name_element').classList.add('d-none');
    type_select.value = "compound";
    fill_substance_formulas('s_1_type', 'compound', 's_1_dict');
    await set_delay();
    set_substance_type('s_1_type', 's_1_dict');
    await set_delay();
    document.getElementById('substance_1_compound').focus();
    document.getElementById('substance_1_compound').blur();
    // setAutoComplete('substance_1_compound', 'compound', 'formula', 's_1_type', 'substance_1_name_compound', 'substance_1_compound');
    // setAutoComplete('substance_1_name_compound', 'compound', 'name', 's_1_type', 'substance_1_name_compound', 'substance_1_compound');
    var comF = document.getElementById('substance_1_compound');
    await set_delay();
    comF.value = 'CH4';
    setSelectedItemName('s_1_type', 'substance_1_name_compound', 'substance_1_compound', 'CH4')
    await set_delay(1);
    // onClick the "Continue" button 
    Continue();
    */