from matplotlib import pyplot as plt

styles = plt.style.available
# print(styles)

# i = 0
# j = 5
# while i <= len(styles):
#     print(styles[i:j])
#     i += 5
#     j += 5

print(f"all styles:{styles}")
for i in range(0,len(styles),5):
    # print(styles[i])
    print(styles[i:i+5])


