def chinesetointeger(chinese):
    check_dir = {
        "零": 0,
        "一": 1,
        "二": 2,
        "三": 3,
        "四": 4,
        "五": 5,
        "六": 6,
        "七": 7,
        "八": 8,
        "九": 9,
        "十": 10,
        "百": 100,
    }
    use_str = chinese[:-1]

    the_number = 0
    if use_str != "":
        if "百" in use_str:
            use_str_count = use_str.split("百")
            the_number = check_dir.get(use_str_count[0]) * check_dir.get("百")

            if "十" in use_str:
                use_str_count_set_one = use_str.split("百")

                use_str_count = use_str_count_set_one[1].split("十")
                if use_str_count[0] != "":
                    #                         print(use_str_count[0])
                    #                         print(use_str_count[1])
                    if use_str_count[1] != "":
                        the_number += check_dir.get(use_str_count[0]) * check_dir.get("十") + check_dir.get(
                            use_str_count[1])
                    else:
                        the_number += check_dir.get(use_str_count[0]) * check_dir.get("十")
                else:
                    the_number += 1 * check_dir.get("十") + check_dir.get(use_str_count[1])

            else:
                use_str_count_set_one = use_str.split("百")

                use_str_count = use_str_count_set_one[1].split("零")
                the_number += check_dir.get(use_str_count[1])


        else:
            if "十" in use_str:
                if use_str != "十":
                    use_str_count = use_str.split("十")
                    if use_str_count[0] != "":
                        #                             print(use_str_count[0])
                        #                             print(use_str_count[1])
                        if use_str_count[1] != "":
                            the_number = check_dir.get(use_str_count[0]) * check_dir.get("十") + check_dir.get(
                                use_str_count[1])
                        else:
                            the_number = check_dir.get(use_str_count[0]) * check_dir.get("十")
                    else:
                        the_number = 1 * check_dir.get("十") + check_dir.get(use_str_count[1])
                else:
                    the_number = 1 * check_dir.get("十")

            else:
                #                     print(use_str)
                the_number = check_dir.get(use_str[0])

    #         print(the_number)
    return the_number

