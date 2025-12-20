# Kartik Mathur's Blog

A clean, minimalist blog built with Pelican and the Flex theme, designed to be simple and focused on content.

**Live Site:** https://kartik.com

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your profile image:**
   - Place a square profile image (e.g., 200x200px) at `content/images/profile.jpg`

3. **Customize the site:**
   - Edit `pelicanconf.py` to update:
     - `AUTHOR` - Your name
     - `SITENAME` - Your blog title  
     - `SITESUBTITLE` - Your blog subtitle
     - `SOCIAL` - Your social media links
     - `SITEURL` in `publishconf.py` - Your GitHub Pages URL

## Development

- **Start development server:**
  ```bash
  make devserver
  ```
  Visit http://localhost:8000

- **Build the site:**
  ```bash
  make html
  ```

- **Clean build files:**
  ```bash
  make clean
  ```

## Content

- **Blog posts:** Add markdown files to `content/`
- **Pages:** Add markdown files to `content/pages/`
- **Images:** Add images to `content/images/`

### Post Format

```markdown
Title: Your Post Title
Date: 2024-01-01
Category: Your Category
Tags: tag1, tag2
Slug: your-post-slug

# Your Content Here

Write your post content in Markdown...
```

## Content Management Workflow

### ✏️ **Editing Existing Pages**
```bash
# 1. Navigate to your blog directory
cd /Users/kartik/kartikblog

# 2. Edit content in content/pages/ or content/ directory
# Pages: content/pages/about.md, content/pages/thoughts.md
# Blog posts: content/welcome-to-my-blog.md

# 3. Test locally (optional)
python3 -m pelican content -o output -s pelicanconf.py
python3 -m pelican -lr content -o output -s pelicanconf.py  # Live reload server

# 4. Deploy to GitHub Pages
python3 -m pelican content -o output -s publishconf.py
python3 -m ghp_import -m "Update [description of changes]" -b gh-pages output
git push origin gh-pages
```

### ➕ **Adding New Pages**
```bash
# 1. Create new markdown file
# For pages: content/pages/new-page.md
# For blog posts: content/new-blog-post.md

# 2. Add front matter (required):
Title: Your Page Title
Date: 2024-12-20
Modified: 2024-12-20

# Your content here...

# 3. Use ABSOLUTE URLs for internal links:
[Link Text](https://kartik.com/pages/other-page.html)

# 4. Deploy (same as editing)
python3 -m pelican content -o output -s publishconf.py
python3 -m ghp_import -m "Add new page: [page name]" -b gh-pages output
git push origin gh-pages
```

### 🔄 **Quick Deploy Script**
You can create a simple script:
```bash
# Save as deploy.sh
python3 -m pelican content -o output -s publishconf.py
python3 -m ghp_import -m "Update blog content" -b gh-pages output
git push origin gh-pages
echo "Deployed! Check https://kartik.com in 2-3 minutes"
```

### 📁 **File Structure**
- **Blog posts**: `content/your-post-name.md`
- **Pages**: `content/pages/page-name.md`
- **Images**: `content/images/image.jpg`
- **Config**: `pelicanconf.py` (local), `publishconf.py` (production)

### ⚠️ **Important Notes**
- Always use **absolute URLs** for internal links
- Wait 2-3 minutes after push for GitHub Pages to update
- Use `publishconf.py` for deployment (not `pelicanconf.py`)
- Images go in `content/images/` and reference as `![alt](https://kartik.com/images/filename.jpg)`

**Your site updates at: https://kartik.com** (or https://kmathur.github.io/kartikblog)

## Customization

- **Styling:** Edit `content/extra/custom.css` for custom styles
- **Theme settings:** Modify the Flex theme configuration in `pelicanconf.py`
- **Layout:** The Flex theme templates are in `themes/flex/`

## Theme Features

This setup uses the Flex theme with custom configurations for:

- Clean, minimal design similar to professional blogs
- Responsive layout
- Social media integration
- Archive and tag pages
- Custom CSS for enhanced styling

Enjoy blogging!
