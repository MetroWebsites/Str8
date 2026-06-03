"""
Comprehensive rewrite of all pages:
- Consistent header (logo + desktop nav + mobile hamburger drawer) on ALL pages
- Consistent full footer (logo + links + socials + copyright) on ALL pages  
- Fix info.astro old gold/red -> teal brand colors
- Fix all image proportions (no stretching)
- Fix mobile hero padding
"""

import re

# ═══════════════════════════════════════════════════
# SHARED CSS BLOCKS
# ═══════════════════════════════════════════════════

HEADER_CSS = """
    /* ═══ SHARED HEADER ═══ */
    header {
      position: fixed;
      top: 0; left: 0;
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
    .header-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.4rem 0;
      transition: padding 0.35s ease;
    }
    header.scrolled .header-inner { padding: 0.15rem 0; }
    .logo-wrap {
      display: flex;
      align-items: center;
      text-decoration: none;
      cursor: pointer;
      flex-shrink: 0;
    }
    .logo-img {
      width: 130px;
      height: auto;
      object-fit: contain;
      display: block;
      image-rendering: -webkit-optimize-contrast;
      transition: width 0.35s ease;
    }
    header.scrolled .logo-img { width: 82px; }
    .site-nav {
      display: flex;
      align-items: center;
      gap: 0.15rem;
    }
    .site-nav a {
      color: rgba(255,255,255,0.75);
      text-decoration: none;
      font-weight: 500;
      font-size: 0.88rem;
      padding: 0.4rem 0.65rem;
      border-radius: 6px;
      transition: color 0.25s, background 0.25s;
      white-space: nowrap;
    }
    .site-nav a:hover { color: #5debdd; background: rgba(93,235,221,0.08); }
    .site-nav a.active { color: #5debdd; }
    .site-nav .nav-cta {
      background: linear-gradient(135deg, #5debdd, #3db8ac);
      color: #060606 !important;
      font-weight: 700;
      border-radius: 50px;
      padding: 0.4rem 1rem;
      margin-left: 0.4rem;
    }
    .site-nav .nav-cta:hover { opacity: 0.88; }
    .nav-hamburger {
      display: none;
      background: none;
      border: 1.5px solid rgba(93,235,221,0.35);
      border-radius: 8px;
      padding: 0.45rem;
      cursor: pointer;
      color: #fff;
      align-items: center;
      justify-content: center;
      transition: border-color 0.3s, background 0.3s;
    }
    .nav-hamburger:hover { border-color: #5debdd; background: rgba(93,235,221,0.08); }
    /* Mobile full-screen drawer */
    .mobile-drawer {
      display: none;
      position: fixed;
      inset: 0;
      z-index: 9999;
      background: rgba(6,6,6,0.98);
      backdrop-filter: blur(20px);
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 0.35rem;
      transform: translateX(100%);
      transition: transform 0.35s cubic-bezier(0.4,0,0.2,1);
    }
    .mobile-drawer.open { transform: translateX(0); }
    .mobile-drawer a {
      color: #fff;
      text-decoration: none;
      font-size: 1.4rem;
      font-weight: 700;
      padding: 0.65rem 2rem;
      border-radius: 12px;
      width: 82%;
      text-align: center;
      transition: background 0.2s, color 0.2s;
    }
    .mobile-drawer a:hover,
    .mobile-drawer a.active { background: rgba(93,235,221,0.12); color: #5debdd; }
    .mobile-drawer .drawer-cta {
      background: linear-gradient(135deg, #5debdd, #3db8ac) !important;
      color: #060606 !important;
      margin-top: 0.75rem;
      border-radius: 50px;
    }
    .drawer-close {
      position: absolute;
      top: 1.25rem;
      right: 1.25rem;
      background: none;
      border: 1.5px solid rgba(255,255,255,0.18);
      border-radius: 8px;
      color: #fff;
      padding: 0.45rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: border-color 0.2s;
    }
    .drawer-close:hover { border-color: #5debdd; }
    @media (max-width: 820px) {
      .site-nav { display: none; }
      .nav-hamburger { display: flex; }
      .mobile-drawer { display: flex; }
      .logo-img { width: 95px; }
      header.scrolled .logo-img { width: 68px; }
    }
    @media (max-width: 480px) {
      .logo-img { width: 80px; }
      header.scrolled .logo-img { width: 60px; }
    }
"""

FOOTER_CSS = """
    /* ═══ SHARED FOOTER ═══ */
    .site-footer {
      background: #0d0d0d;
      border-top: 1px solid rgba(93,235,221,0.12);
      padding: 3.5rem 0 1.5rem;
    }
    .footer-grid {
      display: grid;
      grid-template-columns: 1.5fr 1fr 1fr;
      gap: 2.5rem;
      margin-bottom: 2.5rem;
    }
    .footer-brand img {
      width: 100px;
      height: auto;
      object-fit: contain;
      display: block;
      margin-bottom: 0.75rem;
    }
    .footer-brand p {
      color: rgba(255,255,255,0.55);
      font-size: 0.875rem;
      line-height: 1.7;
      margin-bottom: 1.25rem;
    }
    .footer-col-heading {
      font-weight: 700;
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: #5debdd;
      margin-bottom: 1rem;
    }
    .footer-link-list { list-style: none; display: flex; flex-direction: column; gap: 0.5rem; }
    .footer-link-list a {
      color: rgba(255,255,255,0.55);
      text-decoration: none;
      font-size: 0.875rem;
      transition: color 0.2s;
    }
    .footer-link-list a:hover { color: #5debdd; }
    .footer-socials {
      display: flex;
      gap: 0.6rem;
      flex-wrap: wrap;
    }
    .footer-socials a {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      border: 1px solid rgba(93,235,221,0.22);
      display: flex;
      align-items: center;
      justify-content: center;
      color: rgba(255,255,255,0.65);
      text-decoration: none;
      transition: all 0.25s;
      flex-shrink: 0;
    }
    .footer-socials a:hover {
      background: linear-gradient(135deg,#5debdd,#3db8ac);
      color: #060606;
      border-color: transparent;
      transform: translateY(-2px);
    }
    .footer-divider {
      border: none;
      border-top: 1px solid rgba(255,255,255,0.06);
      margin-bottom: 1.25rem;
    }
    .footer-bottom {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      flex-wrap: wrap;
    }
    .footer-bottom p { color: rgba(255,255,255,0.35); font-size: 0.8rem; }
    .footer-bottom a { color: #5debdd; text-decoration: none; }
    @media (max-width: 820px) {
      .footer-grid { grid-template-columns: 1fr 1fr; gap: 2rem; }
    }
    @media (max-width: 520px) {
      .footer-grid { grid-template-columns: 1fr; gap: 1.75rem; }
      .footer-bottom { flex-direction: column; text-align: center; }
      .site-footer { padding: 2.5rem 0 1.25rem; }
    }
"""

SHARED_JS = """  <script>
    (function() {
      var header = document.getElementById('site-header');
      var hamburger = document.getElementById('hamburgerBtn');
      var drawer = document.getElementById('mobileDrawer');
      var drawerClose = document.getElementById('drawerClose');

      function syncHeaderHeight() {
        if (header) {
          var h = header.getBoundingClientRect().height;
          document.documentElement.style.setProperty('--header-h', h + 'px');
        }
      }

      window.closeMobileDrawer = function() {
        if (drawer) drawer.classList.remove('open');
        document.body.style.overflow = '';
      };

      syncHeaderHeight();
      window.addEventListener('resize', syncHeaderHeight, {passive:true});
      window.addEventListener('scroll', function() {
        if (window.scrollY > 50) { header && header.classList.add('scrolled'); }
        else { header && header.classList.remove('scrolled'); }
        setTimeout(syncHeaderHeight, 380);
      }, {passive:true});

      if (hamburger) hamburger.addEventListener('click', function() {
        if (drawer) drawer.classList.add('open');
        document.body.style.overflow = 'hidden';
      });
      if (drawerClose) drawerClose.addEventListener('click', window.closeMobileDrawer);
      if (drawer) drawer.addEventListener('click', function(e) {
        if (e.target === drawer) window.closeMobileDrawer();
      });
    })();
  </script>"""

def make_header(active=''):
    def nav_link(page, label, href, desktop_extra=''):
        cls = ' class="active"' if active == page else ''
        cls_mob = f' class="active"' if active == page else ''
        return (
            f'        <a href="{href}"{cls}{desktop_extra}>{label}</a>',
            f'    <a href="{href}"{cls_mob} onclick="closeMobileDrawer()">{label}</a>'
        )
    links = [
        nav_link('home',     'Home',     '/'),
        nav_link('services', 'Services', '/services'),
        nav_link('info',     'Info',     '/info'),
        nav_link('team',     'Team',     '/team'),
        nav_link('booking',  'Book',     '/booking'),
        nav_link('donate',   'Donate',   '/donate'),
    ]
    d = '\n'.join(l[0] for l in links)
    m = '\n'.join(l[1] for l in links)
    return f"""  <header id="site-header">
    <div class="container header-inner">
      <a href="/" class="logo-wrap">
        <img src="/_astro/str8-logo-hq-v2.B0dhHdL-.webp"
             onerror="this.onerror=null;this.src='/str8-logo-hq-v2.png'"
             alt="STR8 Positive Thinking" class="logo-img" width="260" height="208" />
      </a>
      <nav class="site-nav">
{d}
        <a href="/#contact" class="nav-cta">Contact</a>
      </nav>
      <button class="nav-hamburger" id="hamburgerBtn" aria-label="Open menu">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </header>

  <div class="mobile-drawer" id="mobileDrawer">
    <button class="drawer-close" id="drawerClose" aria-label="Close">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>
    </button>
{m}
    <a href="/#contact" class="drawer-cta" onclick="closeMobileDrawer()">Contact Us</a>
  </div>"""

FOOTER = """  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="/">
            <img src="/_astro/str8-logo-hq-v2.B0dhHdL-.webp"
                 onerror="this.onerror=null;this.src='/str8-logo-hq-v2.png'"
                 alt="STR8 Positive Thinking" width="200" height="160" />
          </a>
          <p>Spirit-Led Encouragement with Purpose.<br>Causing that good trouble &mdash; <strong style="color:#5debdd;">#GoJesus</strong></p>
          <div class="footer-socials">
            <a href="https://www.youtube.com/@straightpositivethinkingwi1673?sub_confirmation=1" target="_blank" rel="noopener" aria-label="YouTube">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2.5 17a24 24 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49.6 49.6 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24 24 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49.6 49.6 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/></svg>
            </a>
            <a href="https://www.tiktok.com/@steviebennettjr" target="_blank" rel="noopener" aria-label="TikTok">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 8v8a5 5 0 0 1-5 5H8a5 5 0 0 1-5-5V8a5 5 0 0 1 5-5h8a5 5 0 0 1 5 5Z"/><path d="M10 12a3 3 0 1 1-3-3"/><path d="M10 9v8"/><path d="M14 15a3 3 0 0 0 3-3V9a3 3 0 0 1 3-3"/></svg>
            </a>
            <a href="https://www.instagram.com/str8positivethinking" target="_blank" rel="noopener" aria-label="Instagram">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>
            </a>
            <a href="https://podcasters.spotify.com/pod/show/stevie-bennett3" target="_blank" rel="noopener" aria-label="Spotify">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M8 11.8a6 6 0 0 1 8 0"/><path d="M9.5 9a3.5 3.5 0 0 1 5 0"/></svg>
            </a>
            <a href="https://linktr.ee/steviedatroublemaker" target="_blank" rel="noopener" aria-label="Linktree">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3H7a2 2 0 0 0-2 2v5a2 2 0 0 0 2 2h1"/><path d="M17 3h1a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-1"/><path d="M12 3v16"/></svg>
            </a>
          </div>
        </div>
        <div>
          <p class="footer-col-heading">Quick Links</p>
          <ul class="footer-link-list">
            <li><a href="/">Home</a></li>
            <li><a href="/services">Services</a></li>
            <li><a href="/info">About / Info</a></li>
            <li><a href="/team">Our Team</a></li>
            <li><a href="/booking">Book an Event</a></li>
            <li><a href="/donate">Donate</a></li>
            <li><a href="/#contact">Contact Us</a></li>
          </ul>
        </div>
        <div>
          <p class="footer-col-heading">Connect</p>
          <ul class="footer-link-list">
            <li><a href="mailto:info@str8positivethinking.com">info@str8positivethinking.com</a></li>
            <li><a href="/booking">Book a Speaking Event</a></li>
            <li><a href="https://www.tiktok.com/@steviebennettjr" target="_blank" rel="noopener">TikTok @steviebennettjr</a></li>
            <li><a href="https://www.youtube.com/@steviebennett4905/videos" target="_blank" rel="noopener">YouTube Music Ministry</a></li>
          </ul>
        </div>
      </div>
      <hr class="footer-divider" />
      <div class="footer-bottom">
        <p>&copy; {new Date().getFullYear()} Str8 Positive Thinking. All rights reserved.</p>
        <p>Website &amp; SEO by <a href="https://metrowebsites.com" target="_blank" rel="noreferrer">MetroWebsites.com</a></p>
      </div>
    </div>
  </footer>"""

# ═══════════════════════════════════════════════════
# PAGE TRANSFORMS
# ═══════════════════════════════════════════════════

def inject_shared_css_into_style(content, extra_css=''):
    """Append shared header+footer CSS to the first <style> block"""
    # Remove any existing header/footer styles we're replacing
    patterns_to_remove = [
        r'/\* ═══ SHARED HEADER ═══ \*/.*?(?=\n    /\*|\n  </style>)',
        r'/\* ═══ SHARED FOOTER ═══ \*/.*?(?=\n    /\*|\n  </style>)',
    ]
    for p in patterns_to_remove:
        content = re.sub(p, '', content, flags=re.DOTALL)
    
    # Insert before closing </style>
    css_to_add = HEADER_CSS + '\n' + FOOTER_CSS
    if extra_css:
        css_to_add += '\n' + extra_css
    content = content.replace('  </style>\n</head>', css_to_add + '\n  </style>\n</head>', 1)
    return content

def replace_header(content, active=''):
    """Replace everything from <header to </div> (mobile-menu) with new shared header"""
    # Pattern: remove old <header...>...</header> and old mobile menu
    # Then remove old mobile-menu-btn, old mobile drawer blocks
    
    # Remove old mobile menu div blocks (various patterns)
    content = re.sub(
        r'\n  <!-- Mobile Menu -->\s*\n  <div class="mobile-menu"[^>]*>.*?</div>\s*\n',
        '\n', content, flags=re.DOTALL
    )
    content = re.sub(
        r'\n  <div class="mobile-drawer"[^>]*>.*?</div>\s*\n',
        '\n', content, flags=re.DOTALL
    )
    
    # Remove old <header>...</header>
    content = re.sub(r'  <header[^>]*>.*?</header>', '', content, flags=re.DOTALL)
    
    # Insert new header+drawer right after <body>
    content = content.replace('<body>', '<body>\n' + make_header(active), 1)
    return content

def replace_footer(content):
    """Replace old footer with new shared footer"""
    # Remove old footer (handle various patterns)
    content = re.sub(r'\s*<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL)
    # Insert new footer before </body>
    content = content.replace('</body>', '\n' + FOOTER + '\n</body>', 1)
    return content

def replace_scripts(content):
    """Remove old header/drawer scripts and add shared JS"""
    # Remove old syncHeaderHeight script blocks
    content = re.sub(
        r'\s*<script>\s*document\.addEventListener\(\'DOMContentLoaded\'.*?</script>',
        '', content, flags=re.DOTALL
    )
    # Remove old IIFE scripts (like existing shared JS)
    content = re.sub(
        r'\s*<script>\s*\(function\(\).*?</script>',
        '', content, flags=re.DOTALL
    )
    # Add shared JS before </body>
    content = content.replace('</body>', SHARED_JS + '\n</body>', 1)
    return content

def fix_images(content):
    """Fix all images to be proportionate - add object-fit and aspect-ratio constraints"""
    # Fix <img> tags without proper constraints
    # Fix <Image> astro components - ensure height:auto
    content = re.sub(
        r'(style="[^"]*?)height:\s*\d+px([^"]*?")',
        lambda m: m.group(0) if 'width:' not in m.group(0) or 'height:auto' in m.group(0) 
                  else m.group(1) + 'height:auto' + m.group(2),
        content
    )
    # Ensure all astro Image components have height:auto in style
    content = re.sub(
        r'(<Image[^>]+style=")([^"]*)(")([^>]*/>)',
        lambda m: m.group(1) + _ensure_height_auto(m.group(2)) + m.group(3) + m.group(4),
        content
    )
    return content

def _ensure_height_auto(style_str):
    if 'height:auto' not in style_str and 'height: auto' not in style_str:
        if re.search(r'height:\s*\d', style_str):
            style_str = re.sub(r'height:\s*\d+px', 'height:auto', style_str)
    return style_str

# ═══════════════════════════════════════════════════
# INDIVIDUAL PAGE PROCESSORS
# ═══════════════════════════════════════════════════

def process_generic_page(path, active_page=''):
    with open(path) as f:
        content = f.read()
    content = inject_shared_css_into_style(content)
    content = replace_header(content, active_page)
    content = replace_footer(content)
    content = replace_scripts(content)
    content = fix_images(content)
    with open(path, 'w') as f:
        f.write(content)
    print(f'  OK: {path}')

def process_info_page(path):
    """Extra: fix old gold/red color scheme -> teal brand colors"""
    with open(path) as f:
        content = f.read()
    
    # Replace the old :root color vars with new teal brand
    old_root = """:root {
      --gold-gradient: linear-gradient(135deg, #ffd700, #b8860b, #daa520);
      --red-gradient: linear-gradient(135deg, #8b0000, #c00000, #ff0000);
      --gold-glow: 0 0 15px rgba(255, 215, 0, 0.5);
      --red-glow: 0 0 15px rgba(179, 0, 0, 0.5);
      --dark-bg: #0a0a0a;
      --dark-surface: #121212;
      --dark-surface-2: #1a1a1a;
      --text-primary: #ffffff;
      --text-secondary: rgba(255, 255, 255, 0.7);
      --accent-gold: #d4af37;
      --accent-red: #b30000;
      --border-radius: 8px;
    }"""
    new_root = """:root {
      --teal: #5debdd;
      --teal-dark: #3db8ac;
      --teal-gradient: linear-gradient(135deg, #5debdd, #3db8ac);
      --teal-glow: 0 0 18px rgba(93, 235, 221, 0.45);
      --dark-bg: #0a0a0a;
      --dark-surface: #111111;
      --dark-surface-2: #191919;
      --text-primary: #ffffff;
      --text-secondary: rgba(255, 255, 255, 0.7);
      --accent: #5debdd;
      --border-color: rgba(93, 235, 221, 0.18);
      --border-radius: 8px;
    }"""
    content = content.replace(old_root, new_root)
    
    # Replace color usages throughout the page
    replacements = [
        ('var(--gold-gradient)', 'var(--teal-gradient)'),
        ('var(--red-gradient)', 'var(--teal-gradient)'),
        ('var(--gold-glow)', 'var(--teal-glow)'),
        ('var(--red-glow)', 'var(--teal-glow)'),
        ('var(--accent-gold)', 'var(--accent)'),
        ('var(--accent-red)', 'var(--accent)'),
        ('color: var(--accent-gold)', 'color: var(--accent)'),
        ('color: var(--accent-red)', 'color: var(--accent)'),
        ('border-left: 4px solid var(--accent)', 'border-left: 4px solid var(--accent)'),
        # Fix inline gold color references
        ('rgba(212, 175, 55, 0.1)', 'rgba(93, 235, 221, 0.08)'),
        ('rgba(212, 175, 55, 0.2)', 'rgba(93, 235, 221, 0.18)'),
        ('rgba(212, 175, 55, 0.3)', 'rgba(93, 235, 221, 0.25)'),
        ('rgba(212, 175, 55, 0.4)', 'rgba(93, 235, 221, 0.35)'),
        ('rgba(212, 175, 55,', 'rgba(93, 235, 221,'),
        ('#d4af37', '#5debdd'),
        ('color: #d4af37', 'color: #5debdd'),
        # Fix .gold-text and .red-text classes in HTML
        ('class="gold-text"', 'class="teal-text"'),
        ('class="red-text"', 'class="teal-text"'),
        ('.gold-text', '.teal-text'),
        ('.red-text', '.teal-text'),
    ]
    for old, new in replacements:
        content = content.replace(old, new)
    
    # Fix the teal-text CSS (add it if not there)
    content = content.replace(
        '.teal-text {\n      background: var(--teal-gradient)',
        '.teal-text {\n      background: var(--teal-gradient)'
    )
    # Make sure .teal-text is defined
    if '.teal-text' not in content:
        content = content.replace(
            '    .container {',
            '    .teal-text {\n      background: var(--teal-gradient);\n      -webkit-background-clip: text;\n      background-clip: text;\n      color: transparent;\n      display: inline-block;\n    }\n\n    .container {'
        )
    
    # Fix the stretched photo - ensure object-fit:cover and aspect-ratio
    content = re.sub(
        r'(<Image src=\{grinchImage\}[^>]+style=")([^"]*?)(")',
        r'\1width:100%;height:auto;object-fit:contain;border-radius:12px;display:block;\3',
        content
    )
    # Also fix any bare <Image> with just border-radius that could stretch
    content = re.sub(
        r'style="border-radius: 12px; width: 100%; box-shadow:[^"]*"',
        'style="border-radius:12px;width:100%;height:auto;object-fit:cover;display:block;box-shadow:0 20px 40px rgba(0,0,0,0.5);border:1px solid rgba(93,235,221,0.2);"',
        content
    )

    # Fix border on info cards to use teal
    content = re.sub(
        r'border: 1px solid rgba\(212, 175, 55, 0\.\d+\)',
        'border: 1px solid var(--border-color)',
        content
    )
    content = re.sub(
        r'border: 2px solid rgba\(212, 175, 55, 0\.\d+\)',
        'border: 2px solid rgba(93,235,221,0.25)',
        content
    )

    # Run generic transforms
    content_tmp = content
    # Write temp so other functions can read it
    with open(path, 'w') as f:
        f.write(content_tmp)
    
    process_generic_page(path, 'info')

def process_index_page(path):
    """Index page: keep most content, just fix header/footer/mobile/hero"""
    with open(path) as f:
        content = f.read()
    
    # Fix hero section - make sure padding-top uses CSS var
    content = re.sub(
        r'\.hero \{([^}]*?)padding-top:[^;]+;',
        lambda m: '.hero {' + m.group(1) + 'padding-top: var(--header-h, 160px);',
        content
    )
    
    # Fix mobile media query for hero - remove hardcoded padding overrides
    content = re.sub(
        r'\.hero \{\s*min-height: 75vh;\s*\}',
        '.hero { min-height: 75vh; }',
        content
    )
    
    # Inject shared CSS
    content = inject_shared_css_into_style(content)
    
    # Replace header - index has its own custom one with mobile-menu
    content = replace_header(content, 'home')
    
    # Replace footer - index has a big custom footer, replace with shared
    content = replace_footer(content)
    
    # Replace scripts
    content = replace_scripts(content)
    
    # Fix images
    content = fix_images(content)
    
    with open(path, 'w') as f:
        f.write(content)
    print(f'  OK: {path}')

# ═══════════════════════════════════════════════════
# RUN ALL
# ═══════════════════════════════════════════════════

print("Processing pages...")

process_index_page('src/pages/index.astro')
process_info_page('src/pages/info.astro')
process_generic_page('src/pages/booking.astro', 'booking')
process_generic_page('src/pages/donate.astro', 'donate')
process_generic_page('src/pages/team.astro', 'team')
process_generic_page('src/pages/services/index.astro', 'services')
process_generic_page('src/pages/services/wedding-ceremonies.astro', 'services')
process_generic_page('src/pages/services/motivational-speaking.astro', 'services')
process_generic_page('src/pages/services/encouragement-support.astro', 'services')
process_generic_page('src/pages/services/youth-programs.astro', 'services')

print("\nAll pages processed!")
