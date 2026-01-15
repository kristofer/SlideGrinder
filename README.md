# SlideGrinder

A command-line tool that converts PDFs or web articles into presentation slides.

## Description

SlideGrinder takes a PDF file or a URL to a blog post/article and automatically generates a series of presentation slides containing the key points from the input. The tool extracts content, processes it intelligently, and produces clean, ready-to-use slides in both Markdown and HTML formats.

## Features

- 📄 **PDF Support**: Extract content from PDF documents
- 🌐 **URL Support**: Scrape and process content from web articles
- 📊 **Smart Content Processing**: Automatically identifies key points and structures them into slides
- 🎨 **Multiple Formats**: Generates slides in Markdown and HTML formats
- 🔧 **Customizable**: Control number of slides and output format
- 💻 **Simple CLI**: Easy-to-use command-line interface

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Install from source

```bash
git clone https://github.com/kristofer/SlideGrinder.git
cd SlideGrinder
pip install -r requirements.txt
```

Or install in development mode:

```bash
pip install -e .
```

## Usage

### Basic Usage

Process a PDF file:
```bash
python slidegrinder.py document.pdf
```

Process a web article:
```bash
python slidegrinder.py https://example.com/article
```

### Advanced Options

Specify output directory:
```bash
python slidegrinder.py document.pdf -o my_presentation
```

Choose output format:
```bash
python slidegrinder.py https://blog.com/post -f html
```

Control number of slides:
```bash
python slidegrinder.py document.pdf -n 15
```

### Command-Line Arguments

```
positional arguments:
  input                 Input PDF file path or URL

optional arguments:
  -h, --help            Show help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory for slides (default: slides)
  -f {markdown,html,both}, --format {markdown,html,both}
                        Output format (default: both)
  -n NUM_SLIDES, --num-slides NUM_SLIDES
                        Maximum number of slides to generate (default: 10)
```

## Output

SlideGrinder generates:

1. **Markdown file** (`slides.md`): A single file containing all slides in Markdown format
2. **HTML files** (`slide_01.html`, `slide_02.html`, etc.): Individual HTML files for each slide with clean, professional styling
3. **Index file** (`index.html`): A navigation page linking to all slides

All files are saved in the specified output directory (default: `slides/`).

## Examples

### Example 1: Process a research paper PDF
```bash
python slidegrinder.py research_paper.pdf -o research_slides -n 12
```

### Example 2: Create slides from a blog post
```bash
python slidegrinder.py https://medium.com/@author/article -o blog_slides -f html
```

### Example 3: Quick markdown slides
```bash
python slidegrinder.py report.pdf -f markdown
```

## How It Works

1. **Content Extraction**: 
   - For PDFs: Extracts text using PyPDF2
   - For URLs: Fetches and parses HTML content with BeautifulSoup

2. **Content Processing**:
   - Identifies structure and key points
   - Groups related content together
   - Extracts headings and main ideas

3. **Slide Generation**:
   - Creates a title slide
   - Organizes content into logical slides
   - Formats as bullet points
   - Generates clean, readable output

## Dependencies

- `pypdf2` - PDF text extraction
- `beautifulsoup4` - HTML parsing
- `requests` - HTTP requests for URL fetching
- `markdown` - Markdown processing

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Kristofer

## Troubleshooting

**Issue**: "PyPDF2 is required for PDF processing"
- **Solution**: Install dependencies with `pip install -r requirements.txt`

**Issue**: "Could not extract sufficient content"
- **Solution**: Ensure the PDF is text-based (not scanned images) or the URL is accessible

**Issue**: "Error fetching URL"
- **Solution**: Check your internet connection and verify the URL is accessible
