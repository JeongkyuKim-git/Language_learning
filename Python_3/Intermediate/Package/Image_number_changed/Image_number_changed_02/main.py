import package_pro_util

logo = package_pro_util.read_image('image_logo')
text = package_pro_util.read_image('image_text')

print('코드잇 로고:')
# logo를 디스플래이해 주세요
### 코드를 작성해 주세요 ###
package_pro_util.display(logo)

print('\n코드잇 텍스트:')
# text를 디스플래이해 주세요
### 코드를 작성해 주세요 ###
package_pro_util.display(text)

# text를 색상 반전해서 inverted_text에 저장해 주세요
### 코드를 작성해 주세요 ###
inverted_text = package_pro_util.invert(text)

# logo와 text를 합성한 이미지를 merged_img에 저장해 주세요
### 코드를 작성해 주세요 ###
merged_img = package_pro_util.merge(logo, text)

print('\n색상 반전 텍스트:')
# inverted_text를 디스플래이해 주세요
### 코드를 작성해 주세요 ###
package_pro_util.display(inverted_text)
print('\n합성 이미지:')
# merged_img를 디스플래이해 주세요
### 코드를 작성해 주세요 ###
package_pro_util.display(merged_img)

# 채점 코드
print()
key_functions = ['read_image', 'save_image', 'display', 'invert', 'merge']
non_key_functions = ['get_size', 'empty_image', 'invert_bit', 'or_bits']
print(all(x in dir(package_pro_util) for x in key_functions))
print(not any(x in dir(package_pro_util) for x in non_key_functions))