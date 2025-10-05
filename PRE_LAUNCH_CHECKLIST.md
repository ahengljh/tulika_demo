# Pre-Launch Checklist - Professor Tulika Mitra's Website

Complete this checklist before deploying the website to ensure everything is ready.

## ✅ Files & Content

### Required Files
- [x] `index.html` - Main website file
- [x] `styles.css` - Stylesheet with NUS branding
- [x] `script.js` - JavaScript for interactivity
- [x] `nus-logo.svg` - NUS university logo
- [x] `soc-logo.svg` - School of Computing logo
- [x] `profile-placeholder.svg` - Profile image placeholder
- [x] `README.md` - Project documentation
- [x] `DEPLOYMENT_GUIDE.md` - Deployment instructions
- [x] `CONTENT_SUMMARY.md` - Content overview

### Optional Files (Recommended)
- [ ] `favicon-32x32.png` - Website favicon (32x32)
- [ ] `favicon-16x16.png` - Website favicon (16x16)
- [ ] `profile.jpg` or `profile.png` - Real profile photo (400x400)
- [ ] `robots.txt` - Search engine instructions
- [ ] `sitemap.xml` - Site structure for SEO

---

## ✅ Content Verification

### Personal Information
- [x] Name: Tulika Mitra
- [x] Title: Vice Provost (Academic Affairs)
- [x] Title: Provost's Chair Professor of Computer Science
- [x] Institution: National University of Singapore
- [x] Department: School of Computing
- [x] Email: tulika@comp.nus.edu.sg
- [x] Phone: +65 6516-6839
- [x] Office: COM3-02-13, 13 Computing Drive

### External Links (Verify All Work)
- [x] Google Scholar: https://scholar.google.com/citations?user=ajeWJ4UAAAAJ
- [x] DBLP: https://dblp.org/pid/22/5985.html
- [x] eCO Lab: http://www.comp.nus.edu.sg/~eco
- [x] NUS Computing: https://www.comp.nus.edu.sg/
- [x] NUS Main: https://www.nus.edu.sg/

### Publications
- [x] 12 recent publications (2024-2025) included
- [x] All DOI links working
- [x] Author names accurate
- [x] Venue names correct
- [x] Links to DBLP and Google Scholar included

### Research Information
- [x] 3 current research projects described
- [x] 4 research tools listed
- [x] Research focus clearly stated
- [x] eCO Lab mentioned and linked

### Teaching
- [x] 9 courses listed with course codes
- [x] Course descriptions accurate
- [x] Level (UG/Grad) indicated
- [x] Courses match official NUS offerings

### Team
- [x] 5 current PhD students listed
- [x] Student names accurate
- [x] Research areas assigned

---

## ✅ Technical Checks

### HTML Validation
- [ ] Validate at https://validator.w3.org/
  - Should have 0 errors
  - Warnings are acceptable

### CSS Validation
- [ ] Validate at https://jigsaw.w3.org/css-validator/
  - Should have 0 errors
  - Vendor prefix warnings are acceptable

### Browser Testing
- [ ] Chrome (latest version)
- [ ] Firefox (latest version)
- [ ] Safari (latest version)
- [ ] Edge (latest version)

### Mobile Testing
- [ ] iPhone (Safari)
- [ ] Android (Chrome)
- [ ] Tablet (iPad/Android)

### Responsive Design
- [ ] Desktop (1920px+)
- [ ] Laptop (1366px - 1920px)
- [ ] Tablet (768px - 1365px)
- [ ] Mobile (< 768px)

### Functionality Tests
- [ ] Navigation menu works
- [ ] Mobile menu toggles correctly
- [ ] Smooth scrolling to sections
- [ ] Publication filters work (All/2024/2025/Awards)
- [ ] All links open in correct window/tab
- [ ] Email links work
- [ ] Phone number formatted correctly

---

## ✅ SEO & Performance

### SEO Checks
- [x] Title tag present and descriptive
- [x] Meta description (155 characters max)
- [x] Meta keywords included
- [x] Open Graph tags for social media
- [x] Twitter Card tags present
- [x] Structured data (Schema.org JSON-LD)
- [x] Canonical URL set
- [ ] Sitemap.xml created and uploaded

### Performance Tests
- [ ] Test at https://pagespeed.web.dev/
  - Target: Performance > 90
  - Target: Accessibility > 95
  - Target: Best Practices > 90
  - Target: SEO > 95

- [ ] Test at https://gtmetrix.com/
  - Target: Grade A or B
  - Target: Load time < 3 seconds

### Image Optimization
- [x] SVG logos used (already optimized)
- [ ] Profile photo compressed (if added)
- [ ] Images have alt text
- [ ] Favicon created and added

---

## ✅ Security & Privacy

### HTTPS
- [ ] SSL certificate installed
- [ ] All external resources loaded via HTTPS
- [ ] No mixed content warnings

### Privacy
- [ ] No tracking scripts (unless intentionally added)
- [ ] No third-party cookies
- [ ] Email not exposed to spam bots (mailto: links are safe)

### External Resources
- [x] Google Fonts loaded from official CDN
- [x] Font Awesome loaded from official CDN
- [ ] All CDN resources use Subresource Integrity (SRI) if critical

---

## ✅ Accessibility

### WCAG 2.1 Compliance
- [x] Semantic HTML5 elements used
- [x] Headings in logical order (h1 → h2 → h3)
- [x] All images have alt text
- [x] Color contrast ratios meet WCAG AA
- [ ] Test with screen reader (NVDA/JAWS/VoiceOver)
- [ ] Keyboard navigation works (Tab, Enter, Esc)
- [ ] Focus indicators visible

### ARIA
- [x] ARIA labels where needed
- [x] Landmarks properly defined
- [ ] Forms accessible (if added later)

---

## ✅ Content Quality

### Writing & Grammar
- [x] No spelling errors
- [x] Professional tone maintained
- [x] Technical terms used correctly
- [x] Consistent terminology

### Accuracy
- [x] All names spelled correctly
- [x] Titles and affiliations accurate
- [x] Publication details correct
- [x] Contact information current

### Completeness
- [x] All sections complete
- [x] No "Lorem ipsum" placeholder text
- [x] No broken internal links
- [x] No missing images

---

## ✅ Pre-Deployment Tasks

### Before Uploading
- [ ] Create backup of all files
- [ ] Test all files locally in browser
- [ ] Clear browser cache and test again
- [ ] Check file permissions (readable)
- [ ] Verify file names (no spaces, lowercase)

### Recommended Additions
- [ ] Add real profile photo
  - Format: JPG or PNG
  - Size: 400x400 pixels
  - Professional headshot
  - Update path in HTML

- [ ] Create favicons
  ```bash
  # Use online tool: https://realfavicongenerator.net/
  # Or create manually at 32x32 and 16x16
  ```

- [ ] Create robots.txt
  ```txt
  User-agent: *
  Allow: /
  Sitemap: https://yourdomain.com/sitemap.xml
  ```

- [ ] Create sitemap.xml
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
      <loc>https://yourdomain.com/</loc>
      <lastmod>2025-01-XX</lastmod>
      <changefreq>monthly</changefreq>
      <priority>1.0</priority>
    </url>
  </urlset>
  ```

---

## ✅ Deployment Checklist

### Choose Deployment Platform
- [ ] Option 1: Netlify (Recommended)
- [ ] Option 2: GitHub Pages
- [ ] Option 3: Vercel
- [ ] Option 4: Traditional hosting

### Deployment Steps (Netlify)
1. [ ] Create Netlify account
2. [ ] Drag & drop `tulika_demo` folder
3. [ ] Wait for deployment (30 seconds)
4. [ ] Test deployed site
5. [ ] Customize site name
6. [ ] (Optional) Add custom domain
7. [ ] Enable HTTPS (automatic)
8. [ ] Set up form notifications (if added)

### Deployment Steps (GitHub Pages)
1. [ ] Create GitHub account
2. [ ] Create new repository
3. [ ] Upload all files
4. [ ] Enable GitHub Pages in settings
5. [ ] Wait for deployment (1-2 minutes)
6. [ ] Test deployed site
7. [ ] (Optional) Add custom domain
8. [ ] Update DNS if using custom domain

---

## ✅ Post-Deployment

### Immediate Checks (Within 1 Hour)
- [ ] Visit deployed URL
- [ ] Test on mobile device
- [ ] Test all navigation links
- [ ] Verify all external links work
- [ ] Check images load correctly
- [ ] Test email links
- [ ] Verify social media preview
  - Test at: https://www.opengraph.xyz/

### First Week
- [ ] Submit to Google Search Console
- [ ] Submit to Bing Webmaster Tools
- [ ] Monitor for broken links
- [ ] Check browser console for errors
- [ ] Set up Google Analytics (optional)
- [ ] Share with colleagues for feedback

### First Month
- [ ] Review analytics (if enabled)
- [ ] Check search engine indexing
- [ ] Monitor site performance
- [ ] Address any reported issues
- [ ] Update content as needed

---

## ✅ Maintenance Plan

### Monthly Tasks
- [ ] Add new publications
- [ ] Check for broken links
- [ ] Review analytics
- [ ] Update news/announcements (if added)
- [ ] Backup website files

### Semester Tasks
- [ ] Update course information
- [ ] Update team member list
- [ ] Refresh research project descriptions
- [ ] Add new achievements/awards

### Annual Tasks
- [ ] Full content review
- [ ] Update copyright year
- [ ] Review and refresh design
- [ ] Check all external links
- [ ] Update profile photo if needed

---

## ✅ Optional Enhancements

### Nice to Have
- [ ] Add PDF of CV/Resume
- [ ] Create separate publications page
- [ ] Add news/blog section
- [ ] Include photo gallery
- [ ] Add student testimonials
- [ ] Create alumni page
- [ ] Add publication search
- [ ] Include research impact metrics
- [ ] Add upcoming talks/events
- [ ] Create teaching materials section

### Advanced Features
- [ ] Contact form with validation
- [ ] Publication database with filtering
- [ ] Dark mode toggle
- [ ] Multi-language support
- [ ] RSS feed for updates
- [ ] Integration with Google Scholar API
- [ ] Automated publication updates
- [ ] Comment system for blog (if added)

---

## 🎯 Final Pre-Launch Checklist

**Review this list one final time before going live:**

1. [ ] All content is accurate and up-to-date
2. [ ] All links have been tested and work
3. [ ] Site has been tested on multiple devices
4. [ ] Site has been tested on multiple browsers
5. [ ] Site loads quickly (< 3 seconds)
6. [ ] No console errors in browser
7. [ ] SEO meta tags are complete
8. [ ] Contact information is correct
9. [ ] Copyright year is current
10. [ ] You have a backup of all files

---

## 📝 Notes & Issues

Use this space to track any issues or notes during testing:

### Issues Found
-

### Issues Fixed
-

### Future Improvements
-

---

## ✅ Approval

- [ ] Content approved by Professor Mitra
- [ ] Technical review completed
- [ ] All issues resolved
- [ ] Ready for deployment

**Deployment Date**: _______________

**Deployed By**: _______________

**Deployed URL**: _______________

---

## 📞 Support Contacts

**Website Questions**: tulika@comp.nus.edu.sg
**Technical Support**: NUS IT Support
**Domain Issues**: Domain registrar support
**Hosting Issues**: Platform support (Netlify/GitHub/etc.)

---

**Checklist Version**: 1.0.0
**Last Updated**: January 2025

---

## Quick Start Guide

**If you're ready to deploy right now:**

1. Upload the entire `tulika_demo` folder to Netlify Drop
2. Visit: https://app.netlify.com/drop
3. Drag the folder
4. Done! Your site is live in 30 seconds

**For more detailed instructions, see DEPLOYMENT_GUIDE.md**
