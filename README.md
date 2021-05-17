# Meme-Generator

The goal of this project is to build a "meme generator" – a multimedia application to dynamically generate memes, including an image with an overlaid quote. It’s not that simple though! Your content team spent countless hours writing quotes in a variety of filetypes. You could manually copy and paste these quotes into one standard format – but you’re going to over-engineer a solution to load quotes from each file to show off your fancy new Python skills.

What Will I Build?
You have been called on to demonstrate your newly learned skills to create a dynamic data-rich application to generate images with quotes.

The application you build must:

-Interact with a variety of complex filetypes. This emulates the kind of data you’ll encounter in a data engineering role.
-Load quotes from a variety of filetypes (PDF, Word Documents, CSVs, Text files).
Load, manipulate, and save images.
-Accept dynamic user input through a command-line tool and a web service. This emulates the kind of work you’ll encounter as a full stack developer.
This project will give you a hands-on opportunity to practice what you've learned in this course, such as:

-Object-oriented thinking in Python, including abstract classes, class methods, and static methods.
-DRY (don’t repeat yourself) principles of class and method design.
-Working with modules and packages in Python.
-As you're building your project, be sure to demonstrate coding best practices for style and documentation. Ensure your code, docstrings, and comments adhere to PEP 8 Standards.

You'll find detailed instructions on the following pages. And while you work through the instructions, you can also check your work against the project rubric to see exactly what your reviewer will be looking for when they grade your project.

Quote Engine
The Quote Engine module is responsible for ingesting many types of files that contain quotes. For our purposes, a quote contains a body and an author:

"This is a quote body" - Author
This module will be composed of many classes and will demonstrate your understanding of complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles.

Quote Format
Example quotes are provided in a variety of files. Take a moment to review the file formats in ./_data/SimpleLines and ./_data/DogQuotes. Your task is to design a system to extract each quote line-by-line from these files.

Ingestors
An abstract base class, IngestorInterface should define two methods with the following class method signatures:

def can_ingest(cls, path: str) -> boolean
def parse(cls, path: str) -> List[QuoteModel]
Separate strategy objects should realize IngestorInterface for each file type (csv, docx, pdf, txt).

TIP: pdftotext may not be installed on your local machine (Mac or Windows). If this is the case, you can install using the open source XpdfReader utility.

A final Ingestor class should realize the IngestorInterface abstract base class and encapsulate your helper classes. It should implement logic to select the appropriate helper for a given file based on filetype.

NOTE: Do not use the pdftotext PIP Library - we'd like you to demonstrate your understanding of the subprocess module.

Meme Engine Module
The Meme Engine Module is responsible for manipulating and drawing text onto images. It will reinforce your understanding of object-oriented thinking while demonstrating your skill using a more advanced third party library for image manipulation.