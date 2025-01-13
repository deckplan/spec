#!/usr/bin/python3
# SPDX-License-Identifier: Apache-2.0

import filecmp
import os
import tempfile
from itertools import cycle
from pathlib import Path

import mkdocs_gen_files
import oyaml as yaml
from mdutils.mdutils import MdUtils


def write_markdown(file_obj: dict, file_name: str) -> None:
    if "types" in file_obj:
        custom_types = file_obj.pop("types")
        mdFile.new_header(level=2, title="Data Types")
        for type in custom_types:
            for key, value in type.items():
                mdFile.new_line(f"{key}: {value}")

    for function_classification, value in file_obj.items():
        function_classification_str = function_classification.replace("_", " ").title()
        mdFile.new_header(level=2, title=f"{function_classification_str}")
        functions_list = yaml_file_object[function_classification]

        for function_spec in functions_list:
            function_name = function_spec["name"]
            mdFile.new_header(level=3, title=f"{function_name}")

            """
            Write markdown for implementations.

            If names for the function arguments are provided, show function signature with
            the argument names.  Function signature will also include optional arguments.
            """

            EXAMPLE_IMPL = False
            mdFile.new_paragraph("Implementations:")
            implementations_list = function_spec["impls"]
            option_names_list = []
            document_options = []

            for count, impl in enumerate(implementations_list):
                if "args" not in impl:
                    continue
                args_list = impl["args"]
                arg_string = []
                only_arg_names = []
                arg_with_option_names = []
                arg_descriptions = []

                # For each function implementation, collect details on the following:
                #
                # Argument values:
                #   values, value names, description
                for arg in args_list:
                    if "value" in arg:
                        arg_string.append(arg["value"])
                        if "name" in arg:
                            only_arg_names.append(arg["name"])
                            arg_with_option_names.append(arg["name"])
                        if "description" in arg:
                            arg_descriptions.append(arg["description"])
                    elif "options" in arg:
                        choices = str(arg["options"])

                        # enum with no defined name, will be named as the list of choices
                        if "name" in arg:
                            option_name = str(arg["name"])
                        else:
                            option_name = choices

                        # Required enums will be prepended with `req_enum` inside the function
                        arg_string.append(option_name)
                        arg_with_option_names.append(option_name)
                        option_names_list.append(option_name)
                        document_options.append((option_name, choices))
                    else:
                        raise Exception(
                            f"Unrecognized argument found in "
                            f"{file_name}:{function_name}"
                        )

                opts = impl["options"] if "options" in impl else {}
                for opt_name, opt in opts.items():
                    choices = str(opt["values"])
                    document_options.append((opt_name, choices))
                    option_name = f"option:{opt_name}"
                    arg_string.append(option_name)
                    arg_with_option_names.append(option_name)
                    option_names_list.append(option_name)

                # If the implementation is variadic, the last argument will appear `min_args`,
                # number of times in the implementation.
                if "variadic" in impl:
                    min_args = impl["variadic"]["min"]
                    for count in range(min_args - 1):
                        arg_string.append(arg_string[-1])
                        if len(only_arg_names) > 0:
                            only_arg_names.append(only_arg_names[-1])

                arg_values = [f"{x}" for x in arg_string]
                options_and_arg_names = [f"{x}" for x in arg_with_option_names]
                # reset the options names list for the next function implementation.
                option_names_list = []
                options_and_arg_names = [f"`{x}`" for x in options_and_arg_names]
                func_concat_arg_input_names = ", ".join(options_and_arg_names)
                arg_values = [f"`{x}`" for x in arg_values]
                func_concat_arg_input_values = ", ".join(arg_values)

                # Only provide an example implementation using the argument names if argument
                # names are provided and an example implementation doesn't already exist.
                if len(only_arg_names) > 0 and not EXAMPLE_IMPL:
                    mdFile.new_line(
                        f"{function_name}({func_concat_arg_input_names}): -> `return_type` "
                    )
                    for arg_name, arg_desc in zip(only_arg_names, arg_descriptions):
                        mdFile.new_line(f"<li>{arg_name}: {arg_desc}</li>")
                    EXAMPLE_IMPL = True

                # If the return value for the function implementation is multiple lines long,
                # print each line separately. This is the case for some functions in
                # functions_arithmetic_decimal.yaml
                if "\n" in impl["return"]:
                    mdFile.new_line(
                        f"{count}. {function_name}({func_concat_arg_input_values}): -> "
                    )
                    multiline_return_str = "\t" + impl["return"]
                    multiline_return_str = multiline_return_str.replace("\n", "\n\t")
                    mdFile.new_line("\t```")
                    mdFile.new_line(f"{multiline_return_str}")
                    mdFile.new_line("\t```")
                else:
                    mdFile.new_line(
                        f"{count}. {function_name}({func_concat_arg_input_values}): -> "
                        f"`{impl['return']}`"
                    )

            if "description" in function_spec:
                description = function_spec["description"]
                mdFile.new_paragraph(text=f"{description}", bold_italics_code="i")
            """
            Write markdown for options.
            """
            document_options = sorted(list(set(document_options)))
            if len(document_options) > 0:
                mdFile.new_paragraph("<details><summary>Options:</summary>")
                mdFile.write("\n")
                for option_name, options_list in document_options:
                    mdFile.new_line(f"<li>{option_name} {options_list} </li> ")

                mdFile.new_paragraph("</details>")
                mdFile.write("\n")


current_file = Path(__file__).name
cur_path = Path(__file__).resolve()
functions_folder = os.path.join(str(Path(cur_path).parents[3]), "extensions")

# Get a list of all the function yaml files
function_files = []
for file in os.listdir(functions_folder):
    if file.startswith("functions"):
        full_path = os.path.join(functions_folder, file)
        function_files.append(full_path)

current_directory = Path(__file__).resolve().parent
with tempfile.TemporaryDirectory() as temp_directory:
    temp_directory = Path(temp_directory)

    for function_file in function_files:
        with open(function_file) as file:
            yaml_file_object = yaml.load(file, Loader=yaml.FullLoader)

        function_file_name = os.path.basename(function_file)
        function_file_no_extension = os.path.splitext(function_file_name)[0]
        function_category = function_file_no_extension.replace("_", " ").capitalize()

        mdFile = MdUtils(file_name=str(temp_directory / function_file_no_extension))
        mdFile.new_header(level=1, title=f"{function_file_name}")
        mdFile.new_paragraph(
            "This document file is generated for "
            + mdFile.new_inline_link(
                link=f"https://github.com/substrait-io/substrait/tree/main/extensions/"
                f"{function_file_name}",
                text=f"{function_file_name}",
            )
        )

        write_markdown(yaml_file_object, function_file_name)
        mdFile.create_md_file()

        # In order to preview the file with `mkdocs serve` we need to copy the file into a tmp file
        # that is generated by mkdocs_gen_files.open method. However, if we always do that, it will
        # get caught in a loop, so we have to detect changes first.
        in_path = temp_directory / f"{function_file_no_extension}.md"
        out_path = current_directory / f"{function_file_no_extension}.md"
        if not out_path.exists() or not filecmp.cmp(in_path, out_path, shallow=False):
            with open(in_path, "r") as markdown_file:
                with mkdocs_gen_files.open(
                    f"extensions/{function_file_no_extension}.md", "w"
                ) as f:
                    for line in markdown_file:
                        f.write(line)
