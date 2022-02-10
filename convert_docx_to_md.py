import mammoth

with open("LucaMagnasco_CV_EN_pub.docx", "rb") as docx_file:
    result = mammoth.convert_to_markdown(docx_file)
with open("README.md", "w") as markdown_file:
    markdown_file.write(result.value)
