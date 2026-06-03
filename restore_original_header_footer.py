#!/usr/bin/env python3
"""
Restore the original home-page header, footer and JS to ALL pages.
The original (from commit 713c185) is what the user liked.
We replace the new 'site-header / mobile-drawer / site-footer' pattern
with the original 'header / mobile-menu / footer' pattern on every page.
"""

import re, os

# ─────────────────────────────────────────────────────────────────────────────
# 1. ORIGINAL CSS BLOCKS (exactly from 713c185 index.astro)
# ─────────────────────────────────────────────────────────────────────────────

HEADER_CSS = """
    header {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      z-index: 1000;
      background: rgba(6, 6, 6, 0.97);
      backdrop-filter: blur(20px) saturate(180%);
      border-bottom: 1px solid rgba(93, 235, 221, 0.12);
      transition: all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
    }

    header.scrolled {
      background: rgba(6, 6, 6, 0.99);
      box-shadow: 0 2px 24px rgba(0,0,0,0.7);
    }

    .header-content {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.6rem 0;
      transition: padding 0.35s ease;
    }

    header.scrolled .header-content {
      padding: 0.25rem 0;
    }

    .logo-container {
      display: flex;
      align-items: center;
      gap: 1rem;
      cursor: pointer;
      transition: transform 0.3s ease;
    }

    .logo-container:hover {
      transform: translateY(-2px);
    }

    .logo-img {
      width: 160px;
      height: auto;
      border-radius: 0;
      border: none;
      box-shadow: none;
      background: transparent;
      object-fit: contain;
      display: block;
      transition: width 0.35s ease;
      image-rendering: -webkit-optimize-contrast;
      image-rendering: crisp-edges;
    }

    header.scrolled .logo-img {
      width: 100px;
    }

    nav {
      display: flex;
      gap: 2.5rem;
      align-items: center;
    }

    nav a {
      color: var(--text-secondary, #B8B8B8);
      text-decoration: none;
      font-weight: 500;
      font-size: 0.95rem;
      position: relative;
      transition: color 0.3s ease;
    }

    nav a::before {
      content: '';
      position: absolute;
      bottom: -5px;
      left: 0;
      width: 0;
      height: 2px;
      background: linear-gradient(90deg, #5debdd, #3db8ac);
      transition: width 0.3s ease;
    }

    nav a:hover {
      color: #ffffff;
    }

    nav a:hover::before {
      width: 100%;
    }

    nav a.active {
      color: #5debdd;
    }

    nav a.active::before {
      width: 100%;
    }

    .mobile-menu-btn {
      display: none;
      background: none;
      border: none;
      color: #ffffff;
      font-size: 1.5rem;
      cursor: pointer;
      padding: 0.5rem;
    }

    /* Mobile Menu */
    .mobile-menu {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100vh;
      background: #060606;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 2rem;
      z-index: 9999;
      transform: translateX(-100%);
      transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .mobile-menu.open {
      transform: translateX(0);
    }

    .mobile-menu a {
      color: #ffffff;
      text-decoration: none;
      font-size: 1.75rem;
      font-weight: 600;
      transition: color 0.3s ease;
    }

    .mobile-menu a:hover,
    .mobile-menu a.active {
      color: #5debdd;
    }

    .close-menu-btn {
      position: absolute;
      top: 2rem;
      right: 2rem;
      background: none;
      border: none;
      color: #ffffff;
      font-size: 2rem;
      cursor: pointer;
      padding: 0.5rem;
    }

    @media (max-width: 768px) {
      nav {
        display: none;
      }
      .mobile-menu-btn {
        display: block;
      }
      .logo-img {
        width: 80px;
        height: auto;
      }
      header.scrolled .logo-img {
        width: 60px;
      }
    }
"""

FOOTER_CSS = """
    footer {
      background: #0F0F0F;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      padding: 4rem 0 2rem;
    }

    .footer-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 3rem;
      margin-bottom: 3rem;
    }

    .footer-about p {
      color: #B8B8B8;
      margin: 1rem 0;
      line-height: 1.7;
    }

    .footer-heading {
      font-size: 1.25rem;
      margin-bottom: 1.5rem;
      position: relative;
      padding-bottom: 0.75rem;
      color: #ffffff;
    }

    .footer-heading::after {
      content: '';
      position: absolute;
      bottom: 0;
      left: 0;
      width: 50px;
      height: 2px;
      background: linear-gradient(90deg, #5debdd, #3db8ac);
    }

    .footer-links {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .footer-links a {
      color: #B8B8B8;
      text-decoration: none;
      transition: all 0.3s ease;
    }

    .footer-links a:hover {
      color: #5debdd;
      transform: translateX(5px);
    }

    .newsletter-form {
      display: flex;
      gap: 0.75rem;
      flex-wrap: wrap;
    }

    .newsletter-input {
      flex: 1;
      min-width: 160px;
      padding: 0.875rem 1.25rem;
      background: #060606;
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 12px;
      color: #ffffff;
      font-size: 0.95rem;
    }

    .newsletter-input:focus {
      outline: none;
      border-color: #5debdd;
    }

    .newsletter-btn {
      background: linear-gradient(135deg, #5debdd, #3db8ac);
      color: #060606;
      border: none;
      border-radius: 12px;
      padding: 0.875rem 1.75rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.3s ease;
    }

    .newsletter-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 15px rgba(93, 235, 221, 0.5);
    }

    .footer-bottom {
      text-align: center;
      padding-top: 2rem;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
    }

    .footer-bottom p {
      color: #808080;
      font-size: 0.95rem;
    }

    .footer-bottom a {
      color: #5debdd;
      text-decoration: none;
      transition: color 0.3s ease;
    }

    .footer-bottom a:hover {
      color: #3db8ac;
    }

    .social-links {
      display: flex;
      gap: 1rem;
      margin-top: 1rem;
    }

    .social-link {
      color: #B8B8B8;
      transition: color 0.3s ease, transform 0.3s ease;
      display: flex;
      align-items: center;
    }

    .social-link:hover {
      color: #5debdd;
      transform: translateY(-3px);
    }

    .logo-text {
      font-size: 1.1rem;
      font-weight: 700;
      letter-spacing: 0.05em;
    }

    @media (max-width: 768px) {
      .footer-grid {
        gap: 1.5rem;
      }
      footer {
        padding: 2rem 0 1rem;
      }
      .newsletter-form {
        flex-direction: column;
      }
      .newsletter-input {
        width: 100%;
      }
    }
"""

# ─────────────────────────────────────────────────────────────────────────────
# 2. HTML BLOCKS (per-page active link injected by make_header)
# ─────────────────────────────────────────────────────────────────────────────

def make_header(active_page):
    """Return the original header + mobile-menu HTML, with active class on the right link."""
    links = [
        ('/', 'Home'),
        ('/services', 'Services'),
        ('/info', 'Info'),
        ('/team', 'Team'),
        ('/booking', 'Book'),
        ('/donate', 'Donate'),
        ('#contact', 'Contact'),
    ]
    nav_links = ''
    mobile_links = ''
    for href, label in links:
        active = ' class="active"' if href == active_page else ''
        nav_links += f'        <a href="{href}"{active}>{label}</a>\n'
        mobile_links += f'    <a href="{href}"{active}>{label}</a>\n'

    return f"""  <header>
    <div class="container header-content">
      <a href="/" style="display:flex;align-items:center;text-decoration:none;">
        <Image src={{newLogo}} alt="STR8 Positive Thinking Logo" width={{320}} height={{256}} class="logo-img" />
      </a>
      <nav>
{nav_links}      </nav>
      <button class="mobile-menu-btn" aria-label="Open mobile menu">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" x2="20" y1="12" y2="12"/><line x1="4" x2="20" y1="6" y2="6"/><line x1="4" x2="20" y1="18" y2="18"/></svg>
      </button>
    </div>
  </header>

  <!-- Mobile Menu -->
  <div class="mobile-menu">
    <button class="close-menu-btn" aria-label="Close mobile menu">
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
    </button>
{mobile_links}  </div>"""


# The footer uses {new Date().getFullYear()} which is Astro/JSX syntax — keep as-is
FOOTER = """  <footer>
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
            <Image src={newLogo} alt="STR8 Positive Thinking Logo" width={80} height={64} style="object-fit:contain;background:transparent;height:auto;" />
            <div class="logo-text">
              <span class="gradient-text">STR8</span> <span class="gradient-text-red">POSITIVE</span>
            </div>
          </div>
          <p>"Causing that good trouble, we are all about helping people an encouraging them"</p>
          <div class="social-links">
            <a href="https://www.youtube.com/@straightpositivethinkingwi1673?sub_confirmation=1" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2.5 17a24.12 24.12 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.56 49.56 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24.12 24.12 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.55 49.55 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/></svg>
            </a>
            <a href="https://podcasters.spotify.com/pod/show/stevie-bennett3" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Spotify">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M8 11.8a6 6 0 0 1 8 0"/><path d="M9 9a3.5 3.5 0 0 1 6 0"/><path d="M11 6a1.5 1.5 0 1 1 2 0"/></svg>
            </a>
            <a href="https://www.tiktok.com/@steviebennettjr" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="TikTok">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 8v8a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5V8a5 5 0 0 1 5-5h8a5 5 0 0 1 5 5Z"/><path d="M10 12a3 3 0 1 1-3-3"/><path d="M10 9v8"/><path d="M14 15a3 3 0 0 0 3-3V9a3 3 0 0 1 3-3"/></svg>
            </a>
            <a href="https://www.instagram.com/str8positivethinking?igshid=ZDdkNTZiNTM%3D" class="social-link" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>
            </a>
          </div>
        </div>

        <div>
          <h4 class="footer-heading">Quick Links</h4>
          <div class="footer-links">
            <a href="/">Home</a>
            <a href="/services">All Services</a>
            <a href="/info">About Us</a>
            <a href="/team">Meet the Team</a>
            <a href="/booking">Book an Event</a>
            <a href="/donate">Donate</a>
            <a href="/#contact">Contact Us</a>
          </div>
        </div>

        <div>
          <h4 class="footer-heading">Subscribe to Our Newsletter</h4>
          <p style="color: #B8B8B8; margin-bottom: 1rem;">Stay updated with our latest events and positive messages</p>
          <form data-form-type="utility" action="https://metrowebsites.com/api/submit-form/" method="POST" enctype="multipart/form-data" class="newsletter-form">
            <input type="email" name="email" class="newsletter-input" placeholder="Your email address" required />
            <button type="submit" class="newsletter-btn">Subscribe</button>
            <input type="hidden" name="form_name" value="Newsletter Signup" />
          </form>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; {new Date().getFullYear()} Str8 Positive Thinking. All rights reserved. | <a href="https://metrowebsites.com" target="_blank" rel="noreferrer">Website and SEO by <strong>MetroWebsites.com</strong></a></p>
      </div>
    </div>
  </footer>"""


# ─────────────────────────────────────────────────────────────────────────────
# 3. JAVASCRIPT (original from 713c185)
# ─────────────────────────────────────────────────────────────────────────────

SHARED_JS = """  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const header = document.querySelector('header');
      const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
      const mobileMenu = document.querySelector('.mobile-menu');
      const closeMenuBtn = document.querySelector('.close-menu-btn');

      // Set CSS var --header-h to actual header height so hero padding always matches
      function syncHeaderHeight() {
        if (header) {
          const h = header.getBoundingClientRect().height;
          document.documentElement.style.setProperty('--header-h', h + 'px');
        }
      }
      syncHeaderHeight();
      window.addEventListener('resize', syncHeaderHeight, { passive: true });

      // Header scroll effect — shrinks logo + padding when scrolled
      window.addEventListener('scroll', () => {
        if (window.scrollY > 60) {
          header?.classList.add('scrolled');
        } else {
          header?.classList.remove('scrolled');
        }
        // Re-sync after transition settles
        setTimeout(syncHeaderHeight, 380);
      }, { passive: true });

      // Mobile menu toggle
      mobileMenuBtn?.addEventListener('click', () => {
        mobileMenu?.classList.add('open');
        document.body.style.overflow = 'hidden';
      });

      closeMenuBtn?.addEventListener('click', () => {
        mobileMenu?.classList.remove('open');
        document.body.style.overflow = '';
      });

      // Close mobile menu when clicking a link
      const mobileLinks = mobileMenu?.querySelectorAll('a');
      mobileLinks?.forEach(link => {
        link.addEventListener('click', () => {
          mobileMenu?.classList.remove('open');
          document.body.style.overflow = '';
        });
      });
    });
  </script>"""


# ─────────────────────────────────────────────────────────────────────────────
# 4. HELPER: strip old shared-CSS blocks injected by fix_all_pages.py
# ─────────────────────────────────────────────────────────────────────────────

def strip_injected_shared_css(content):
    """Remove the HEADER_CSS and FOOTER_CSS blocks that were injected before </style>."""
    # These markers were added by fix_all_pages.py
    content = re.sub(
        r'\n\s*/\* ={10,} SHARED HEADER CSS ={10,} \*/.*?/\* ={10,} END SHARED HEADER CSS ={10,} \*/',
        '', content, flags=re.DOTALL
    )
    content = re.sub(
        r'\n\s*/\* ={10,} SHARED FOOTER CSS ={10,} \*/.*?/\* ={10,} END SHARED FOOTER CSS ={10,} \*/',
        '', content, flags=re.DOTALL
    )
    # Also strip site-header / site-footer / mobile-drawer / drawer-* / nav-hamburger CSS rules
    patterns_to_strip = [
        r'\s*#site-header\s*\{[^}]*\}',
        r'\s*\.site-nav\s*\{[^}]*\}',
        r'\s*\.site-nav\s+a\s*\{[^}]*\}',
        r'\s*\.site-nav\s+a\.active\s*\{[^}]*\}',
        r'\s*\.nav-hamburger\s*\{[^}]*\}',
        r'\s*\.nav-hamburger\s*:hover\s*\{[^}]*\}',
        r'\s*\.mobile-drawer\s*\{[^}]*\}',
        r'\s*\.mobile-drawer\.open\s*\{[^}]*\}',
        r'\s*\.mobile-drawer\s+a\s*\{[^}]*\}',
        r'\s*\.mobile-drawer\s+a\s*:hover\s*\{[^}]*\}',
        r'\s*\.mobile-drawer\s+a\.active\s*\{[^}]*\}',
        r'\s*\.drawer-close\s*\{[^}]*\}',
        r'\s*\.drawer-cta\s*\{[^}]*\}',
        r'\s*\.logo-wrap\s*\{[^}]*\}',
        r'\s*\.header-inner\s*\{[^}]*\}',
        r'\s*\.site-footer\s*\{[^}]*\}',
        r'\s*\.footer-brand\s*\{[^}]*\}',
        r'\s*\.footer-socials\s*\{[^}]*\}',
        r'\s*\.footer-socials\s+a\s*\{[^}]*\}',
        r'\s*\.footer-col-heading\s*\{[^}]*\}',
        r'\s*\.footer-link-list\s*\{[^}]*\}',
        r'\s*\.footer-link-list\s+li\s*\{[^}]*\}',
        r'\s*\.footer-link-list\s+a\s*\{[^}]*\}',
        r'\s*\.footer-link-list\s+a\s*:hover\s*\{[^}]*\}',
        r'\s*\.footer-divider\s*\{[^}]*\}',
        r'\s*\.nav-cta\s*\{[^}]*\}',
        r'\s*\.nav-cta\s*:hover\s*\{[^}]*\}',
    ]
    for pat in patterns_to_strip:
        content = re.sub(pat, '', content, flags=re.DOTALL)
    return content


# ─────────────────────────────────────────────────────────────────────────────
# 5. MAIN PROCESSOR
# ─────────────────────────────────────────────────────────────────────────────

def inject_css_into_style(content, css_to_add):
    """Inject CSS just before the closing </style> tag."""
    return content.replace('</style>', css_to_add + '\n  </style>', 1)


def replace_header_and_mobile(content, active_page):
    """Replace new bad header+drawer block with original header+mobile-menu."""
    new_header_html = make_header(active_page)

    # Pattern 1: new-style  <header id="site-header"> ... </header> \n\n  <div class="mobile-drawer" ...> ... </div>
    pattern = re.compile(
        r'  <header id="site-header">.*?</header>\s*\n\s*<div class="mobile-drawer"[^>]*>.*?</div>',
        re.DOTALL
    )
    replaced, n = re.subn(pattern, new_header_html, content)
    if n:
        print(f"  ✓ Replaced new site-header+drawer pattern ({n} match)")
        return replaced

    # Pattern 2: already has old-style <header> — just update the active links
    pattern2 = re.compile(r'  <header>.*?</div>\s*\n\s*<!-- Mobile Menu -->\s*\n\s*<div class="mobile-menu">.*?</div>', re.DOTALL)
    replaced2, n2 = re.subn(pattern2, new_header_html, content)
    if n2:
        print(f"  ✓ Updated active link in existing original header ({n2} match)")
        return replaced2

    print("  ⚠ No header pattern matched!")
    return content


def replace_footer(content):
    """Replace new bad site-footer block with original footer."""
    # Pattern: <footer class="site-footer"> ... </footer>
    pattern = re.compile(r'  <footer class="site-footer">.*?</footer>', re.DOTALL)
    replaced, n = re.subn(pattern, FOOTER, content)
    if n:
        print(f"  ✓ Replaced site-footer ({n} match)")
        return replaced

    # Already has old-style <footer> (no class="site-footer") — replace it too
    pattern2 = re.compile(r'  <footer>.*?</footer>', re.DOTALL)
    replaced2, n2 = re.subn(pattern2, FOOTER, content)
    if n2:
        print(f"  ✓ Replaced plain <footer> ({n2} match)")
        return replaced2

    print("  ⚠ No footer pattern matched!")
    return content


def replace_scripts(content):
    """Replace the new IIFE script block with the original DOMContentLoaded script."""
    # New-style script starts with (function() { and references site-header / hamburgerBtn
    pattern = re.compile(
        r'  <script>\s*\(function\(\)\s*\{.*?closeMobileDrawer.*?\}\)\(\);\s*</script>',
        re.DOTALL
    )
    replaced, n = re.subn(pattern, SHARED_JS, content)
    if n:
        print(f"  ✓ Replaced new IIFE script ({n} match)")
        return replaced

    # Already has old-style script — update to ensure body overflow handling is present
    # (Just leave it if it already has DOMContentLoaded — it's the right one)
    if 'DOMContentLoaded' in content and 'syncHeaderHeight' in content:
        print("  ✓ Script already in original form, skipping")
        return content

    print("  ⚠ No script pattern matched!")
    return content


def ensure_logo_import(content, is_services_page=False):
    """Make sure newLogo is imported from the correct relative path."""
    # Services pages need ../../assets/
    asset_path = '../../assets/str8-logo-hq-v2.png' if is_services_page else '../assets/str8-logo-hq-v2.png'

    if 'newLogo' not in content:
        # Add import
        content = content.replace(
            "import { Image } from 'astro:assets';",
            f"import {{ Image }} from 'astro:assets';\nimport newLogo from '{asset_path}';"
        )
        print(f"  ✓ Added newLogo import")
    return content


def process_page(filepath, active_page, is_services=False):
    print(f"\nProcessing: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ensure newLogo import exists
    content = ensure_logo_import(content, is_services_page=is_services)

    # 2. Strip any old injected shared-CSS blocks
    content = strip_injected_shared_css(content)

    # 3. Inject clean original CSS into <style> block
    # First remove any existing header/footer CSS blocks that were already there
    # (they may already be correct for index.astro, so we remove and re-add to be safe)
    content = re.sub(r'\n\s*/\* --- header styles --- \*/.*', '', content, flags=re.DOTALL)

    # Inject original header + footer CSS before </style>
    content = inject_css_into_style(content, HEADER_CSS + FOOTER_CSS)

    # 4. Replace bad header HTML with original
    content = replace_header_and_mobile(content, active_page)

    # 5. Replace bad footer HTML with original
    content = replace_footer(content)

    # 6. Replace bad script with original
    content = replace_scripts(content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✓ Done: {filepath}")


# ─────────────────────────────────────────────────────────────────────────────
# 6. RUN ON ALL PAGES
# ─────────────────────────────────────────────────────────────────────────────

PAGES = [
    ('src/pages/index.astro',                              '/',          False),
    ('src/pages/info.astro',                               '/info',      False),
    ('src/pages/booking.astro',                            '/booking',   False),
    ('src/pages/donate.astro',                             '/donate',    False),
    ('src/pages/team.astro',                               '/team',      False),
    ('src/pages/services/index.astro',                     '/services',  True),
    ('src/pages/services/wedding-ceremonies.astro',        '/services',  True),
    ('src/pages/services/motivational-speaking.astro',     '/services',  True),
    ('src/pages/services/encouragement-support.astro',     '/services',  True),
    ('src/pages/services/youth-programs.astro',            '/services',  True),
]

if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    for rel_path, active, is_svc in PAGES:
        full_path = os.path.join(base, rel_path)
        process_page(full_path, active, is_svc)
    print("\n✅ All pages processed!")
