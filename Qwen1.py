import dashscope
import sys
from dashscope import Generation
from OCR import extract_text_from_images

dashscope.api_key = "sk-7fb20e6fc3ac4834a14e2b044926bdcf"


# 定义调用大模型的函数
def get_response(messages):
    response = Generation.call(model="qwen-turbo",
                               messages=messages,
                               result_format='message')
    return response


# 构建提取关键信息的prompt
def build_prompt(drug_info, Info):
    # 基础prompt部分
    base_prompt = "你是一名医学顾问，现在需要你提取药品说明书中最关键的信息，"

    # 添加年龄段信息
    if 'age' in Info:
        base_prompt += f"以最通俗易懂的简洁话语告诉{Info['age']}患者药的用法。"
    else:
        base_prompt += "以最通俗易懂的简洁话语告诉患者药的用法。"

    # 开始构建详细指令
    detailed_prompt = "总结用于UI介绍的文本，每个条目要占一行,格式一定统一："
    detailed_prompt += "1. **用于UI展示的文本：** "
    for option in Info['optionInfo']:
        detailed_prompt += f"{option}："
    # 添加其他用户选项信息
    if 'others' in Info:
        detailed_prompt += f" 其他需要回答的问题：{Info['others']}。"

    detailed_prompt += "\n总结用于语音播报的文本，这里不要分条："
    detailed_prompt += "2. **用于语音播报的文稿：** 请用口语化的方式概述药品的"
    for option in Info['optionInfo']:
        detailed_prompt += f"{option}、"

    detailed_prompt = detailed_prompt.rstrip('、')
    detailed_prompt += "，注意信息的连贯性和易理解性，适合语音播放。"



    # 构建完整的Prompt
    prompt = [
        {'role': 'system', 'content': base_prompt},
        {'role': 'user', 'content': f'以下是药品说明书的内容：\n\n{drug_info}\n\n **特别注意**下列两段总结文本的开头'
                                    f'**用于UI展示的文本：**和**用于语音播报的文稿：**不能擅自改变其内容，因为涉及到后期匹配的问题。**请确保不擅自修改两个标题**\n'
                                    f'{detailed_prompt}'}
    ]
    return prompt


# 从药品说明书文本中提取关键信息并格式化输出
def extract_drug_info(drug_info_text, Info):
    messages = build_prompt(drug_info_text, Info)
    response = get_response(messages)
    assistant_output = response.output.choices[0]['message']['content']
    ui_text, speech_text = split_response(assistant_output)
    return ui_text, speech_text

# 分割模型返回的文本，提取用于UI和语音播报的部分
def split_response(content):
    start_ui = content.find("用于UI展示的文本：")
    start_speech = content.find("用于语音播报的文稿：")
    if start_ui == -1 or start_speech == -1:
        sys.exit()
        # print("未找到预期的标签，无法正确分割文本。")
        # return "", ""
    # 提取对应部分的文本并格式化
    ui_end = start_speech if start_speech > start_ui else len(content)
    ui_text = content[start_ui + len("**用于UI展示的文本：**"):ui_end-4].strip()
    speech_text = content[start_speech + len("**用于语音播报的文稿：**"):].strip()
    ui_text = ui_text.replace("*","")
    ui_text = ui_text[:-1]
    speech_text = speech_text.replace("*","")
    # 格式化UI文本
    formatted_ui_text = format_ui_text(ui_text)

    return formatted_ui_text, speech_text

# 对UI文本进行进一步格式化处理,分行
def format_ui_text(ui_text):
    # 将UI文本分行
    lines = ui_text.split('\n')
    formatted_lines = []
    for line in lines:
        if '保质期' in line:
            formatted_lines.append(f"保质期：{line.split('：')[-1]}")
        elif '生产日期' in line:
            formatted_lines.append(f"生产日期：{line.split('：')[-1]}")
        else:
            formatted_lines.append(line)
    return '\n'.join(formatted_lines)


# 直接返回提取的信息,总发送函数（即将图片传输给大模型并识别文字，后总结的重要函数）
def get_drug_info_from_images(img_path, Info):
    texts = extract_text_from_images(img_path)
    ui_text, speech_text = extract_drug_info(texts, Info)
    return ui_text, speech_text
