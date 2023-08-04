import re
import sys
import os

def extract_figure_labels(tex_content):
    # Regular expression pattern to match \label{...} inside \begin{figure} ... \end{figure} environment
    figure_label_pattern = r'\\begin{figure}.*?\\label{([^}]+)}.*?\\end{figure}'
    
    # Find all matches of the figure label pattern in the TeX content
    figure_labels = re.findall(figure_label_pattern, tex_content, re.DOTALL)
    
    return figure_labels

def extract_table_labels(tex_content):
    figure_label_pattern = r'\\begin{longtable}.*?\\label{([^}]+)}.*?\\end{longtable}'
    
    # Find all matches of the figure label pattern in the TeX content
    figure_labels = re.findall(figure_label_pattern, tex_content, re.DOTALL)
    
    return figure_labels

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py path/to/your/tex/file.tex path/to/your/replace/tex/file.tex")
        sys.exit(1)
    
    tex_file_path = sys.argv[1]
    replace_tex_file_path = sys.argv[2]
    
    try:
        with open(tex_file_path, 'r') as tex_file:
            tex_content = tex_file.read()
    except FileNotFoundError:
        print(f"Error: The file '{tex_file_path}' does not exist.")
        sys.exit(1)
    
    template = r"sed -i 's/\\ref{ref}/{num}/g' " + replace_tex_file_path

    # figures
    figure_labels = extract_figure_labels(tex_content)
    
    print("Figure labels in order of appearance:")
    for index, label in enumerate(figure_labels, start=1):
        command = template.format(ref="{" + label + "}", num=str(index))
        print(command)
        os.system(command)
    print()

    # tables
    figure_labels = extract_table_labels(tex_content)
    
    print("Table labels in order of appearance:")
    for index, label in enumerate(figure_labels, start=1):
        command = template.format(ref="{" + label + "}", num=str(index))
        print(command)
        os.system(command)
