import numpy as np


    ''' *** temp hold on np.array processing *** '''
    # tcl_b = np.array(triple_candidate_list)
    # for item in tcl_b:
    #     nums = item
    #     row_1 = nums[0]
    #     col_1 = nums[1]
    #     sq_1 = nums[2]
    #     print("1189 ", row_1, col_1, sq_1)
    #     # Problem: get the last 2 or 3 numbers, can't get them from the end
    #     # because the length of nums depends on the number of double digit 
    #     #rows and columns. 
    #     # Solution, find the index of the third comma and add 2 and 3
    #     # if position 4 is not a "]" it is a number to be considered.
    #     my_list = nums.tolist()
    #     # Position 8 is guarenteed to find the last comma
    #     c_idx = my_list.index(",", 8) 
    #     print("1192 ", my_list, c_idx)
    #     num_0 = nums[c_idx + 2]
    #     num_1 = nums[c_idx + 3]
    #     if nums[c_idx + 4] != "]":
    #         num_2 = nums[c_idx + 4]
    #         print("1199 ", item, nums, num_0, num_1, num_2)
    #     else:
    #         print("1192 ", item, nums, num_0, num_1)
    #     for item in tcl_b:
    #         nums = item
    #         my_list = nums.tolist()
    #         c_idx = my_list.index(",", 8)
    #         num_4 = nums[c_idx + 2]
    #         num_5 = nums[c_idx + 3]
    #         if nums[c_idx + 4] != "]":
    #             num_6 = nums[c_idx + 4]
    #             print("1178 ", item, nums, num_4, num_5, num_6)
    #         else:
    #             print("1180 ", item, nums, num_4, num_5)

    # convert to a np array
    # tcl_a = np.array([['1', '6', '2', '8AC'], ['1', '10', '3', '6A']])
    # l_tcl_a = len(tcl_a)
    # tcl_set = set()
    # nums0 = tcl_a[0][3]
    # l = len(nums0)
    # print("1136 tcl_a is ", tcl_a, l_tcl_a)
    # print("1137 num0 is ", nums0, ",", l)
    # print("1137 num0 parts are ", nums0[0], nums0[1], nums0[2])
    # tcl_set.add(nums0[0])
    # tcl_set.add(nums0[1])
    # tcl_set.add(nums0[2])
    # print("1144 tcl_set is ", tcl_set, len(tcl_set))
    # nums1 = tcl_a[1][3]
    # l = len(nums1)
    # tcl_set.add(nums1[0])
    # tcl_set.add(nums1[1])
    # if l == 3:
    #     tcl_set.add(nums1[2])
    # print("1151 tcl_set is ", tcl_set, len(tcl_set))
    # print("343 len(not_done_arefs) is ", len(not_done_arefs))
