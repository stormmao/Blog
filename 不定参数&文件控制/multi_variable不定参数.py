- 对于 python 文件来说，Tab 键在共享的场景中就是灾难。不同平台对 Tab 键的展开空格是不一样的，会导致缩进错误，代码无法运行。所以最好使用4个空格
来保持缩进，这样不容易出错.
def variable(rounds_num, *param, w_num, weight_limit, stp_filename):
    length = len(param)
    n = length % 3

    if n != 0:
        print("ERROR:Please check your input!")
    else:
        name_num = int(length / 3)
        print("Successful!")
        with open(stp_filename, 'w') as stp_file:
            x = ""
            w = ""
            for num in range(name_num):
                for i in range(rounds_num * param[3 * num + 2] + param[3 * num + 2]):
                    x += "{0}{1},".format(param[3 * num], i)
                stp_file.write(x[:-1])
                stp_file.write(": BITVECTOR({0});\n".format(param[3 * num + 1]))
                x = ""

            w = ["w{0}".format(i) for i in range(w_num * rounds_num)]
            round_sum = ""

            for p in w:
                round_sum += p + ","

            stp_file.write(round_sum[:-1])
            stp_file.write(": BITVECTOR({0});\n".format(16))
            stp_file.write("weight: BITVECTOR(16);\n")

            # if len(p) > 1:
            #     stp_file.write("ASSERT(weight = BVPLUS({},{}));\n".format(16, round_sum[:-1]))
            # else:
            #     stp_file.write("ASSERT(weight = {});\n".format(round_sum[:-1]))

            stp_file.write("ASSERT(weight = {0:#018b});\n".format(weight_limit))

variable(4, 'x', 8, 10, 'y', 8, 8, 'z', 8, 8, 'q', 8, 8, w_num=16, weight_limit=20,
stp_filename='/Users/maoxiangjie/PycharmProjects/democode/pp4.stp')
