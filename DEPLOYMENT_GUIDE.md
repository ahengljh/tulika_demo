# Deployment Guide - Professor Tulika Mitra's Website

This guide provides step-by-step instructions to deploy the academic website.

## Quick Start (5 minutes)

The fastest way to get your site live:

### Option 1: Netlify Drop (Recommended for Beginners)

1. Go to [https://app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag the entire `tulika_demo` folder onto the page
3. Your site is now live! Netlify will give you a URL like `https://random-name-12345.netlify.app`
4. (Optional) Click "Site settings" to customize the URL or add a custom domain

**No account needed!** Your site will stay live for free.

### Option 2: GitHub Pages (Best for Long-term)

1. Create a GitHub account at [https://github.com](https://github.com)
2. Create a new repository called `tulika-mitra-website`
3. Upload all files from the `tulika_demo` folder
4. Go to **Settings** > **Pages**
5. Under "Source", select **main** branch
6. Click **Save**
7. Your site will be live at `https://yourusername.github.io/tulika-mitra-website`

---

## Detailed Deployment Options

## Option A: Netlify (Easiest - No Coding Required)

### Why Choose Netlify?
- ✅ Free forever
- ✅ Automatic HTTPS
- ✅ Custom domain support
- ✅ Continuous deployment
- ✅ No server management

### Step-by-Step:

1. **Create a Netlify Account**
   - Go to [netlify.com](https://www.netlify.com)
   - Sign up with GitHub, GitLab, or email

2. **Deploy via Drag & Drop**
   - Click "Add new site" > "Deploy manually"
   - Drag the entire `tulika_demo` folder
   - Wait 30 seconds for deployment

3. **Customize Your URL**
   - Click "Site settings" > "Change site name"
   - Choose something like `tulika-mitra` or `prof-tulika-mitra`
   - Your URL becomes `https://tulika-mitra.netlify.app`

4. **Add Custom Domain (Optional)**
   - Click "Domain settings" > "Add custom domain"
   - Follow the instructions to point your domain
   - Netlify provides free SSL certificate

### Updating the Site:
Just drag and drop the updated folder again!

---

## Option B: GitHub Pages (Best for Version Control)

### Why Choose GitHub Pages?
- ✅ Free forever
- ✅ Built-in version control
- ✅ Easy to update via Git
- ✅ Custom domain support
- ✅ Automatic HTTPS

### Step-by-Step:

1. **Create GitHub Account**
   - Go to [github.com](https://github.com)
   - Sign up for free

2. **Create New Repository**
   - Click the "+" icon > "New repository"
   - Name: `tulika-mitra-website` (or any name)
   - Make it **Public**
   - Click "Create repository"

3. **Upload Files**

   **Method 1: Web Interface (Easier)**
   - Click "uploading an existing file"
   - Drag all files from `tulika_demo` folder
   - Click "Commit changes"

   **Method 2: Git Command Line**
   ```bash
   cd /Users/ljh/Downloads/tulika_demo
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/yourusername/tulika-mitra-website.git
   git push -u origin main
   ```

4. **Enable GitHub Pages**
   - Go to repository **Settings**
   - Click **Pages** in left sidebar
   - Under "Source", select **main** branch
   - Click **Save**
   - Wait 1-2 minutes

5. **Access Your Site**
   - Your site will be at: `https://yourusername.github.io/tulika-mitra-website`

6. **Add Custom Domain (Optional)**
   - In Pages settings, add your custom domain
   - Update your domain's DNS settings:
     ```
     Type: CNAME
     Name: www (or @)
     Value: yourusername.github.io
     ```

### Updating the Site:
1. Make changes to your files locally
2. Go to your GitHub repository
3. Click "Upload files" or use Git:
   ```bash
   git add .
   git commit -m "Updated publications"
   git push
   ```

---

## Option C: Vercel (Similar to Netlify)

### Step-by-Step:

1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Click "Add New" > "Project"
4. Import your GitHub repository (or drag & drop)
5. Click "Deploy"
6. Your site is live at `https://yourproject.vercel.app`

---

## Option D: Traditional Web Hosting

### If you already have web hosting (cPanel, Bluehost, etc.):

1. **Access Your Hosting Control Panel**
   - Log in to cPanel or your hosting dashboard

2. **Upload Files via File Manager**
   - Navigate to `public_html` folder
   - Upload all files from `tulika_demo` folder
   - Ensure folder structure is maintained

3. **Or Use FTP**
   - Download an FTP client (FileZilla recommended)
   - Connect using your hosting credentials
   - Upload all files to `public_html` or `www` directory

4. **Access Your Site**
   - Visit your domain: `https://yourdomain.com`

---

## Post-Deployment Checklist

After deploying, verify these items:

### ✅ Content Verification
- [ ] All images load correctly
- [ ] All external links work (Google Scholar, DBLP, etc.)
- [ ] Contact information is correct
- [ ] Publications display properly
- [ ] Course information is accurate

### ✅ Technical Verification
- [ ] Site loads on mobile devices
- [ ] HTTPS is enabled (padlock icon in browser)
- [ ] All pages are accessible
- [ ] Navigation menu works
- [ ] Forms (if any) submit correctly

### ✅ SEO Verification
- [ ] Google Search Console setup
- [ ] Sitemap submitted
- [ ] Meta tags display correctly in social media previews
- [ ] Analytics tracking (if needed)

---

## Adding a Custom Domain

### For .edu.sg or .com.sg domains:

1. **Purchase Domain** (if needed)
   - Recommended: Namecheap, Google Domains, or your university

2. **Update DNS Settings**

   For **Netlify**:
   ```
   Type: CNAME
   Name: www
   Value: yoursitename.netlify.app

   Type: A
   Name: @
   Value: 75.2.60.5
   ```

   For **GitHub Pages**:
   ```
   Type: CNAME
   Name: www
   Value: yourusername.github.io

   Type: A (add all four):
   Name: @
   Values:
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```

3. **Add Domain in Hosting Platform**
   - Go to your Netlify/GitHub Pages settings
   - Add your custom domain
   - Enable "Force HTTPS"

4. **Wait for DNS Propagation**
   - Takes 1-48 hours (usually < 1 hour)
   - Check status at [dnschecker.org](https://dnschecker.org)

---

## Updating Content

### Updating Publications

1. Open `index.html`
2. Find the `<!-- Publications Section -->`
3. Copy an existing publication item and modify:

```html
<div class="publication-item" data-year="2025">
    <div class="pub-year">2025</div>
    <div class="pub-content">
        <h4>Your Paper Title Here</h4>
        <p class="pub-authors">Author1, Author2, Tulika Mitra</p>
        <p class="pub-venue">Conference/Journal Name, 2025</p>
        <div class="pub-links">
            <a href="https://doi.org/..." target="_blank" class="pub-link">DOI</a>
            <a href="paper.pdf" target="_blank" class="pub-link">PDF</a>
        </div>
    </div>
</div>
```

### Updating Team Members

1. Open `index.html`
2. Find the `<!-- Team Section -->`
3. Add/modify team members:

```html
<div class="team-member">
    <div class="member-photo">
        <i class="fas fa-user-circle"></i>
    </div>
    <h4>Student Name</h4>
    <p>Research area: Topic</p>
</div>
```

### Updating Courses

1. Open `index.html`
2. Find the `<!-- Teaching Section -->`
3. Modify course information as needed

---

## Performance Optimization

### Compressing Images

If you add photos:

1. Use [TinyPNG.com](https://tinypng.com) to compress images
2. Resize photos to appropriate dimensions:
   - Profile photo: 400x400px
   - Team photos: 300x300px
   - Research images: 800x600px

### Testing Performance

- Google PageSpeed Insights: [pagespeed.web.dev](https://pagespeed.web.dev)
- GTmetrix: [gtmetrix.com](https://gtmetrix.com)

Target scores:
- Performance: > 90
- Accessibility: > 95
- Best Practices: > 90
- SEO: > 95

---

## Setting Up Analytics (Optional)

### Google Analytics 4

1. Create account at [analytics.google.com](https://analytics.google.com)
2. Get your Measurement ID (G-XXXXXXXXXX)
3. Add to `index.html` before `</head>`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## Troubleshooting

### Site Not Loading

**Problem**: Page shows 404 error
- **Solution**: Check that `index.html` is in the root directory
- **Solution**: Verify deployment completed successfully

**Problem**: Styles not loading
- **Solution**: Ensure `styles.css` is in the same directory as `index.html`
- **Solution**: Check browser console for errors (F12)

### Images Not Displaying

**Problem**: Logos or images don't show
- **Solution**: Verify all SVG files are uploaded
- **Solution**: Check file paths in HTML are correct
- **Solution**: Ensure files aren't blocked by browser security

### Mobile Display Issues

**Problem**: Site looks broken on mobile
- **Solution**: Clear browser cache
- **Solution**: Test in multiple browsers
- **Solution**: Validate HTML at [validator.w3.org](https://validator.w3.org)

---

## Maintenance Schedule

### Weekly
- Check that all external links still work
- Monitor site performance

### Monthly
- Update publications as papers are published
- Check for broken links
- Review analytics (if enabled)

### Semester
- Update course information
- Update team member list
- Refresh research project descriptions

### Annually
- Review and update all content
- Update copyright year in footer
- Check for security updates

---

## Security Best Practices

1. **Always use HTTPS**
   - Netlify and GitHub Pages provide this automatically

2. **Keep Dependencies Updated**
   - Font Awesome CDN updates automatically
   - Google Fonts updates automatically

3. **Monitor for Spam**
   - If you add contact forms, use reCAPTCHA

4. **Regular Backups**
   - GitHub automatically backs up your code
   - Download a local copy monthly

---

## Getting Help

### Resources
- **HTML/CSS**: [W3Schools.com](https://www.w3schools.com)
- **GitHub Pages**: [docs.github.com/pages](https://docs.github.com/pages)
- **Netlify Docs**: [docs.netlify.com](https://docs.netlify.com)

### Support Contacts
- **NUS IT Support**: For university-related hosting
- **Web Hosting Provider**: For technical server issues
- **Domain Registrar**: For DNS and domain issues

---

## Recommended Next Steps

After successful deployment:

1. ✅ **Submit to search engines**
   - [Google Search Console](https://search.google.com/search-console)
   - [Bing Webmaster Tools](https://www.bing.com/webmasters)

2. ✅ **Create sitemap**
   - Use [xml-sitemaps.com](https://www.xml-sitemaps.com)
   - Upload sitemap.xml to root directory

3. ✅ **Set up monitoring**
   - [UptimeRobot](https://uptimerobot.com) - Free uptime monitoring
   - [Google Analytics](https://analytics.google.com) - Traffic tracking

4. ✅ **Add to academic profiles**
   - Update Google Scholar profile with website link
   - Add to NUS faculty directory
   - Update DBLP profile

5. ✅ **Social media**
   - Share on LinkedIn
   - Add to Twitter/X profile
   - Include in email signature

---

## Cost Breakdown

| Platform | Cost | Custom Domain | HTTPS | Bandwidth |
|----------|------|---------------|-------|-----------|
| Netlify | Free | Free | Free | 100GB/month |
| GitHub Pages | Free | Free | Free | 100GB/month |
| Vercel | Free | Free | Free | 100GB/month |
| Traditional Hosting | $3-10/month | Varies | Varies | Varies |

**Recommendation**: Start with Netlify or GitHub Pages (both free and excellent).

---

**Questions?** Contact tulika@comp.nus.edu.sg

**Last Updated**: January 2025
