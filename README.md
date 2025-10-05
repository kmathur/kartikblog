# My Blog

A clean, minimalist blog built with Pelican and the Flex theme, designed to be simple and focused on content.

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

## Deployment to GitHub Pages

### Automatic (Recommended)

1. Push your code to GitHub
2. Enable GitHub Pages in repository settings
3. The GitHub Actions workflow will automatically build and deploy your site

### Manual

```bash
make github
```

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
