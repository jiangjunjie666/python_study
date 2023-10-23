def translate_rna_to_protein(rna):
    protein_sequence = ""
    i = 0

    while i < len(rna):
        codon = rna[i:i+3]  # 从RNA中获取三个碱基的密码子
        amino_acid = PROTEIN_DICT[codon]  # 使用字典查找对应的氨基酸

        if amino_acid == 'Stop':
            break  # 如果遇到停止密码子，停止翻译

        protein_sequence += amino_acid
        i += 3  # 移动到下一个密码子

    return protein_sequence


# 使用示例
rna_sequence = 'UGCGAUGAAUGGGCUCGCUCC'
protein_result = translate_rna_to_protein(rna_sequence)
print(protein_result)
