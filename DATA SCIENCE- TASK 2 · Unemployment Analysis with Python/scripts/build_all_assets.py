import os

# Definition of the AURA Logo Assets

def get_symbol_svg(variant="color", width=1000, height=1000, show_bg=False):
    """
    Variants:
    - 'color': Vibrant cyber-indigo and ultraviolet gradients with luminous depth
    - 'black': Pure monochrome #09090b with precision 14px negative space counter-channels
    - 'white': Pure reversed #ffffff with precision 14px negative space counter-channels
    """
    
    if variant == "color":
        defs = """
    <defs>
      <!-- Gradient 1: Left Ascent (Cyan to Royal Electric Blue) -->
      <linearGradient id="gradAscent" x1="0%" y1="100%" x2="60%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE" />
        <stop offset="45%" stop-color="#0284C7" />
        <stop offset="100%" stop-color="#4F46E5" />
      </linearGradient>

      <!-- Gradient 2: Right Descent (Electric Blue to Deep Royal Violet) -->
      <linearGradient id="gradDescent" x1="40%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#4F46E5" />
        <stop offset="50%" stop-color="#7C3AED" />
        <stop offset="100%" stop-color="#9333EA" />
      </linearGradient>

      <!-- Gradient 3: Horizon Möbius Bridge (Ultraviolet across to Radiant Sky) -->
      <linearGradient id="gradBridge" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#38BDF8" />
        <stop offset="35%" stop-color="#6366F1" />
        <stop offset="70%" stop-color="#8B5CF6" />
        <stop offset="100%" stop-color="#D946EF" />
      </linearGradient>

      <!-- Gradient 4: Subtle Ambient Ray Highlight -->
      <linearGradient id="gradHighlight" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.35" />
        <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.0" />
      </linearGradient>

      <!-- Optical Depth Drop Shadow -->
      <filter id="auraShadow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="24" stdDeviation="32" flood-color="#4F46E5" flood-opacity="0.32" />
      </filter>
    </defs>
    """
        left_fill = "url(#gradAscent)"
        right_fill = "url(#gradDescent)"
        bridge_fill = "url(#gradBridge)"
        bevel_fill = "url(#gradHighlight)"
        filter_attr = 'filter="url(#auraShadow)"'
    elif variant == "black":
        defs = ""
        left_fill = "#09090B"
        right_fill = "#09090B"
        bridge_fill = "#09090B"
        bevel_fill = "#09090B"
        filter_attr = ""
    elif variant == "white":
        defs = ""
        left_fill = "#FFFFFF"
        right_fill = "#FFFFFF"
        bridge_fill = "#FFFFFF"
        bevel_fill = "#FFFFFF"
        filter_attr = ""

    bg_elem = ""
    if show_bg:
        bg_fill = "#090D16" if variant in ["color", "white"] else "#F8FAFC"
        bg_elem = f'<rect width="{width}" height="{height}" fill="{bg_fill}" />\n'

    # Precise geometric facets for the Dimensional Möbius Apex:
    # Tuned for high visual impact, mathematical harmony, and 14px optical gaps
    if variant == "color":
        facets = f"""
    <!-- Left Ascending Pillar -->
    <path d="M 500 155 L 435 155 L 205 725 L 325 725 L 475 355 L 500 240 Z" fill="{left_fill}" />
    
    <!-- Right Descending Pillar -->
    <path d="M 500 155 L 565 155 L 795 725 L 675 725 L 525 355 L 500 240 Z" fill="{right_fill}" />
    
    <!-- Horizon Möbius Crossbar (The Ambient Bridge) -->
    <path d="M 290 535 L 710 535 L 645 635 L 355 635 Z" fill="{bridge_fill}" />
    
    <!-- Optical Apex Core Diamond (Ambient Light Anchor) -->
    <polygon points="500,240 540,340 500,440 460,340" fill="url(#gradHighlight)" opacity="0.85" />
    
    <!-- Subtle Inner Bevel for Tactile Depth -->
    <polygon points="500,155 475,355 500,240" fill="url(#gradHighlight)" />
    """
    else:
        # Monochrome variants with precision cut-out counterforms for crisp printing/etching
        facets = f"""
    <!-- Left Ascending Pillar (with optical negative space channels) -->
    <path d="M 490 165 L 435 165 L 215 725 L 315 725 L 465 375 L 490 270 Z" fill="{left_fill}" />
    
    <!-- Right Descending Pillar -->
    <path d="M 510 165 L 565 165 L 785 725 L 685 725 L 535 375 L 510 270 Z" fill="{right_fill}" />
    
    <!-- Horizon Möbius Crossbar (isolated by 16px negative space gaps) -->
    <path d="M 320 540 L 680 540 L 630 625 L 370 625 Z" fill="{bridge_fill}" />

    <!-- Central Focal Diamond -->
    <polygon points="500,300 530,370 500,440 470,370" fill="{left_fill}" />
    """

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  {defs}
  {bg_elem}
  <g id="aura-symbol" {filter_attr}>
    {facets}
  </g>
</svg>"""
    return svg


def get_horizontal_lockup_svg(variant="color", width=2400, height=800, show_bg=False):
    """
    Horizontal Lockup:
    - Symbol Mark on the left (500x500 box, scaled and positioned at x=140, y=150)
    - Bespoke Vector Typography: 'A U R A' with geometric precision and generous tracking
    - Tagline / Category Descriptor: 'AMBIENT INTELLIGENCE'
    """
    
    if variant == "color":
        defs = """
    <defs>
      <linearGradient id="gradAscentH" x1="0%" y1="100%" x2="60%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE" />
        <stop offset="45%" stop-color="#0284C7" />
        <stop offset="100%" stop-color="#4F46E5" />
      </linearGradient>
      <linearGradient id="gradDescentH" x1="40%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#4F46E5" />
        <stop offset="50%" stop-color="#7C3AED" />
        <stop offset="100%" stop-color="#9333EA" />
      </linearGradient>
      <linearGradient id="gradBridgeH" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#38BDF8" />
        <stop offset="35%" stop-color="#6366F1" />
        <stop offset="70%" stop-color="#8B5CF6" />
        <stop offset="100%" stop-color="#D946EF" />
      </linearGradient>
      <linearGradient id="gradHighlightH" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.35" />
        <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.0" />
      </linearGradient>
      <linearGradient id="gradText" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#F8FAFC" />
        <stop offset="100%" stop-color="#E2E8F0" />
      </linearGradient>
      <filter id="hGlow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#4F46E5" flood-opacity="0.3" />
      </filter>
    </defs>
    """
        text_fill = "#0F172A" if not show_bg and variant == "color_light" else "#F8FAFC"
        tag_fill = "#64748B" if not show_bg and variant == "color_light" else "#94A3B8"
        bg_fill = "#090D16"
        symbol_left = "url(#gradAscentH)"
        symbol_right = "url(#gradDescentH)"
        symbol_bridge = "url(#gradBridgeH)"
        symbol_high = "url(#gradHighlightH)"
        filter_attr = 'filter="url(#hGlow)"'
    elif variant == "black":
        defs = ""
        text_fill = "#09090B"
        tag_fill = "#52525B"
        bg_fill = "#FFFFFF"
        symbol_left = "#09090B"
        symbol_right = "#09090B"
        symbol_bridge = "#09090B"
        symbol_high = "#09090B"
        filter_attr = ""
    elif variant == "white":
        defs = ""
        text_fill = "#FFFFFF"
        tag_fill = "#A1A1AA"
        bg_fill = "#090D16"
        symbol_left = "#FFFFFF"
        symbol_right = "#FFFFFF"
        symbol_bridge = "#FFFFFF"
        symbol_high = "#FFFFFF"
        filter_attr = ""

    bg_elem = f'<rect width="{width}" height="{height}" fill="{bg_fill}" />\n' if show_bg else ""

    # Symbol scaled and translated
    # Origin at (150, 150), scaling down from 1000 to 500 (scale 0.5)
    # Target symbol box: x=140..640, y=150..650
    if variant == "color":
        symbol_content = f"""
      <path d="M 500 155 L 435 155 L 205 725 L 325 725 L 475 355 L 500 240 Z" fill="{symbol_left}" />
      <path d="M 500 155 L 565 155 L 795 725 L 675 725 L 525 355 L 500 240 Z" fill="{symbol_right}" />
      <path d="M 290 535 L 710 535 L 645 635 L 355 635 Z" fill="{symbol_bridge}" />
      <polygon points="500,240 540,340 500,440 460,340" fill="{symbol_high}" opacity="0.85" />
      <polygon points="500,155 475,355 500,240" fill="{symbol_high}" />
      """
    else:
        symbol_content = f"""
      <path d="M 490 165 L 435 165 L 215 725 L 315 725 L 465 375 L 490 270 Z" fill="{symbol_left}" />
      <path d="M 510 165 L 565 165 L 785 725 L 685 725 L 535 375 L 510 270 Z" fill="{symbol_right}" />
      <path d="M 320 540 L 680 540 L 630 625 L 370 625 Z" fill="{symbol_bridge}" />
      <polygon points="500,300 530,370 500,440 470,370" fill="{symbol_left}" />
      """

    # Pure Vector Wordmark Paths for 'A U R A':
    # Converted to 100% geometric paths so it renders identically everywhere without needing font installation!
    # Base height = 240px, baseline at y=460.
    # Letter spacing = 110px.
    # Letter 1: 'A' (x: 820..1060)
    # Letter 2: 'U' (x: 1180..1420)
    # Letter 3: 'R' (x: 1540..1790)
    # Letter 4: 'A' (x: 1910..2150)
    
    # Let's craft exact geometric path data for the 4 letters:
    wordmark_paths = f"""
    <g id="wordmark" fill="{text_fill}">
      <!-- Letter 1: A (Starts at 820) -->
      <path d="
        M 940 220 
        L 970 220 
        L 1070 470 
        L 1005 470 
        L 980 405 
        L 930 405 
        L 905 470 
        L 840 470 
        Z 
        M 955 285 
        L 940 350 
        L 970 350 
        Z
      " />

      <!-- Letter 2: U (Starts at 1160) -->
      <path d="
        M 1160 220 
        L 1225 220 
        L 1225 385 
        C 1225 415, 1245 428, 1275 428 
        C 1305 428, 1325 415, 1325 385 
        L 1325 220 
        L 1390 220 
        L 1390 385 
        C 1390 445, 1345 480, 1275 480 
        C 1205 480, 1160 445, 1160 385 
        Z
      " />

      <!-- Letter 3: R (Starts at 1480) -->
      <path d="
        M 1480 220 
        L 1610 220 
        C 1665 220, 1700 245, 1700 295 
        C 1700 335, 1675 360, 1630 368 
        L 1715 470 
        L 1635 470 
        L 1560 375 
        L 1545 375 
        L 1545 470 
        L 1480 470 
        Z 
        M 1545 272 
        L 1545 325 
        L 1600 325 
        C 1625 325, 1635 315, 1635 298 
        C 1635 282, 1625 272, 1600 272 
        Z
      " />

      <!-- Letter 4: A (Starts at 1790) -->
      <path d="
        M 1910 220 
        L 1940 220 
        L 2040 470 
        L 1975 470 
        L 1950 405 
        L 1900 405 
        L 1875 470 
        L 1810 470 
        Z 
        M 1925 285 
        L 1910 350 
        L 1940 350 
        Z
      " />
    </g>

    <!-- Descriptor / Tagline: AMBIENT INTELLIGENCE -->
    <text x="825" y="555" 
          font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" 
          font-size="44" 
          font-weight="600" 
          letter-spacing="14" 
          fill="{tag_fill}">AMBIENT INTELLIGENCE</text>
    """

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  {defs}
  {bg_elem}
  <!-- Symbol Subgroup -->
  <g transform="translate(140, 150) scale(0.5)" {filter_attr}>
    {symbol_content}
  </g>
  <!-- Wordmark Subgroup -->
  {wordmark_paths}
</svg>"""
    return svg


def get_vertical_lockup_svg(variant="color", width=1200, height=1400, show_bg=False):
    """
    Vertical / Stacked Lockup:
    - Symbol Mark centered at top (x=300, y=140, 600x600)
    - Centered Wordmark 'AURA' (y=890)
    - Centered Tagline 'AMBIENT INTELLIGENCE' (y=980)
    """
    if variant == "color":
        defs = """
    <defs>
      <linearGradient id="gradAscentV" x1="0%" y1="100%" x2="60%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE" />
        <stop offset="45%" stop-color="#0284C7" />
        <stop offset="100%" stop-color="#4F46E5" />
      </linearGradient>
      <linearGradient id="gradDescentV" x1="40%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#4F46E5" />
        <stop offset="50%" stop-color="#7C3AED" />
        <stop offset="100%" stop-color="#9333EA" />
      </linearGradient>
      <linearGradient id="gradBridgeV" x1="0%" y1="0%" x2="100%" y2="0%">
        <stop offset="0%" stop-color="#38BDF8" />
        <stop offset="35%" stop-color="#6366F1" />
        <stop offset="70%" stop-color="#8B5CF6" />
        <stop offset="100%" stop-color="#D946EF" />
      </linearGradient>
      <linearGradient id="gradHighlightV" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.35" />
        <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.0" />
      </linearGradient>
      <filter id="vGlow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="24" stdDeviation="32" flood-color="#4F46E5" flood-opacity="0.32" />
      </filter>
    </defs>
    """
        text_fill = "#F8FAFC"
        tag_fill = "#94A3B8"
        bg_fill = "#090D16"
        symbol_left = "url(#gradAscentV)"
        symbol_right = "url(#gradDescentV)"
        symbol_bridge = "url(#gradBridgeV)"
        symbol_high = "url(#gradHighlightV)"
        filter_attr = 'filter="url(#vGlow)"'
    elif variant == "black":
        defs = ""
        text_fill = "#09090B"
        tag_fill = "#52525B"
        bg_fill = "#FFFFFF"
        symbol_left = "#09090B"
        symbol_right = "#09090B"
        symbol_bridge = "#09090B"
        symbol_high = "#09090B"
        filter_attr = ""
    elif variant == "white":
        defs = ""
        text_fill = "#FFFFFF"
        tag_fill = "#A1A1AA"
        bg_fill = "#090D16"
        symbol_left = "#FFFFFF"
        symbol_right = "#FFFFFF"
        symbol_bridge = "#FFFFFF"
        symbol_high = "#FFFFFF"
        filter_attr = ""

    bg_elem = f'<rect width="{width}" height="{height}" fill="{bg_fill}" />\n' if show_bg else ""

    if variant == "color":
        symbol_content = f"""
      <path d="M 500 155 L 435 155 L 205 725 L 325 725 L 475 355 L 500 240 Z" fill="{symbol_left}" />
      <path d="M 500 155 L 565 155 L 795 725 L 675 725 L 525 355 L 500 240 Z" fill="{symbol_right}" />
      <path d="M 290 535 L 710 535 L 645 635 L 355 635 Z" fill="{symbol_bridge}" />
      <polygon points="500,240 540,340 500,440 460,340" fill="{symbol_high}" opacity="0.85" />
      <polygon points="500,155 475,355 500,240" fill="{symbol_high}" />
      """
    else:
        symbol_content = f"""
      <path d="M 490 165 L 435 165 L 215 725 L 315 725 L 465 375 L 490 270 Z" fill="{symbol_left}" />
      <path d="M 510 165 L 565 165 L 785 725 L 685 725 L 535 375 L 510 270 Z" fill="{symbol_right}" />
      <path d="M 320 540 L 680 540 L 630 625 L 370 625 Z" fill="{symbol_bridge}" />
      <polygon points="500,300 530,370 500,440 470,370" fill="{symbol_left}" />
      """

    # Center-aligned wordmark
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  {defs}
  {bg_elem}
  <!-- Centered Symbol: x=300..900, y=140..740 (scale 0.6) -->
  <g transform="translate(300, 120) scale(0.6)" {filter_attr}>
    {symbol_content}
  </g>
  
  <!-- Centered Wordmark A U R A -->
  <text x="600" y="870" 
        text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" 
        font-size="124" 
        font-weight="700" 
        letter-spacing="28" 
        fill="{text_fill}">AURA</text>

  <!-- Centered Descriptor -->
  <text x="600" y="950" 
        text-anchor="middle"
        font-family="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" 
        font-size="34" 
        font-weight="600" 
        letter-spacing="16" 
        fill="{tag_fill}">AMBIENT INTELLIGENCE</text>
</svg>"""
    return svg


def get_app_icon_svg(width=1024, height=1024):
    """
    Apple & Android Squircle App Icon:
    - 1024x1024 with continuous 22.5% corner radius
    - Deep obsidian glass background with subtle inner border glow
    - Glowing 3D embossed Aura mark centered with optical balance
    """
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <!-- Background Dark Mesh -->
    <radialGradient id="iconBg" cx="50%" cy="30%" r="80%">
      <stop offset="0%" stop-color="#1E293B" />
      <stop offset="60%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#020617" />
    </radialGradient>

    <!-- Glass Rim Glow -->
    <linearGradient id="rimGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#818CF8" stop-opacity="0.2" />
      <stop offset="100%" stop-color="#A855F7" stop-opacity="0.4" />
    </linearGradient>

    <!-- Inner Ambient Spotlight -->
    <radialGradient id="spotlight" cx="50%" cy="45%" r="50%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.25" />
      <stop offset="60%" stop-color="#6366F1" stop-opacity="0.1" />
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0.0" />
    </radialGradient>

    <!-- Mark Gradients -->
    <linearGradient id="iconAscent" x1="0%" y1="100%" x2="60%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="45%" stop-color="#0284C7" />
      <stop offset="100%" stop-color="#4F46E5" />
    </linearGradient>
    <linearGradient id="iconDescent" x1="40%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F46E5" />
      <stop offset="50%" stop-color="#7C3AED" />
      <stop offset="100%" stop-color="#9333EA" />
    </linearGradient>
    <linearGradient id="iconBridge" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="35%" stop-color="#6366F1" />
      <stop offset="70%" stop-color="#8B5CF6" />
      <stop offset="100%" stop-color="#D946EF" />
    </linearGradient>
    <linearGradient id="iconHighlight" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.45" />
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.0" />
    </linearGradient>

    <filter id="iconShadow" x="-30%" y="-30%" width="160%" height="160%">
      <feDropShadow dx="0" dy="28" stdDeviation="36" flood-color="#00F2FE" flood-opacity="0.35" />
      <feDropShadow dx="0" dy="16" stdDeviation="20" flood-color="#7C3AED" flood-opacity="0.4" />
    </filter>

    <clipPath id="squircleClip">
      <rect x="0" y="0" width="1024" height="1024" rx="230" ry="230" />
    </clipPath>
  </defs>

  <!-- Masked Squircle Body -->
  <g clip-path="url(#squircleClip)">
    <!-- Base Fill -->
    <rect width="1024" height="1024" fill="url(#iconBg)" />
    <!-- Ambient Core Spotlight -->
    <rect width="1024" height="1024" fill="url(#spotlight)" />

    <!-- Centered Aura Mark: 620x620 at x=202, y=202 (scale 0.62) -->
    <g transform="translate(202, 202) scale(0.62)" filter="url(#iconShadow)">
      <path d="M 500 155 L 435 155 L 205 725 L 325 725 L 475 355 L 500 240 Z" fill="url(#iconAscent)" />
      <path d="M 500 155 L 565 155 L 795 725 L 675 725 L 525 355 L 500 240 Z" fill="url(#iconDescent)" />
      <path d="M 290 535 L 710 535 L 645 635 L 355 635 Z" fill="url(#iconBridge)" />
      <polygon points="500,240 540,340 500,440 460,340" fill="url(#iconHighlight)" opacity="0.9" />
      <polygon points="500,155 475,355 500,240" fill="url(#iconHighlight)" />
    </g>

    <!-- Inner Border Glow -->
    <rect x="2" y="2" width="1020" height="1020" rx="228" ry="228" fill="none" stroke="url(#rimGlow)" stroke-width="4" opacity="0.8" />
  </g>
</svg>"""
    return svg


def get_construction_grid_svg(width=1600, height=1200):
    """
    Technical Vector Construction Sheet:
    - Demonstrates strict mathematical grid alignment (Fibonacci / Golden Ratio)
    - 60-degree isometric coordinate axes
    - Circular tangent arcs
    - Clearspace rules (X-height margin box)
    - RGB / HEX color callouts
    """
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
  <defs>
    <pattern id="gridPattern" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255, 255, 255, 0.04)" stroke-width="1" />
    </pattern>
    <linearGradient id="gridGradLeft" x1="0%" y1="100%" x2="60%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="100%" stop-color="#4F46E5" />
    </linearGradient>
    <linearGradient id="gridGradRight" x1="40%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#4F46E5" />
      <stop offset="100%" stop-color="#9333EA" />
    </linearGradient>
    <linearGradient id="gridGradBridge" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#D946EF" />
    </linearGradient>
  </defs>

  <!-- Obsidian Blueprint Background -->
  <rect width="{width}" height="{height}" fill="#090D16" />
  <rect width="{width}" height="{height}" fill="url(#gridPattern)" />

  <!-- Technical Header -->
  <text x="80" y="90" font-family="monospace" font-size="28" font-weight="700" fill="#38BDF8" letter-spacing="4">AURA &#x2022; GEOMETRIC CONSTRUCTION &amp; CLEARSPACE SYSTEM</text>
  <text x="80" y="125" font-family="monospace" font-size="14" fill="#64748B" letter-spacing="2">SPECIFICATION: GOLDEN RATIO (&#x3C6; = 1.618) &#x2022; ISOMETRIC AXIS: 60&#xB0; &#x2022; CLEARSPACE UNIT: X = 0.5H</text>

  <!-- Clearspace Boundary Box (X Margin = 90px around 600px mark) -->
  <!-- Mark centered at x=800, y=620, scale=0.7 (dimensions 700x700 centered) -->
  <g transform="translate(450, 220) scale(0.7)">
    <!-- Clearspace Box -->
    <rect x="80" y="40" width="840" height="780" fill="none" stroke="#F43F5E" stroke-width="2" stroke-dasharray="8 8" opacity="0.6" />
    <text x="100" y="70" font-family="monospace" font-size="22" fill="#F43F5E">CLEARSPACE = 1X</text>
    <text x="840" y="70" font-family="monospace" font-size="22" fill="#F43F5E">1X</text>

    <!-- Construction Circles (Golden Ratio & Tangents) -->
    <circle cx="500" cy="500" r="380" fill="none" stroke="#0284C7" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.4" />
    <circle cx="500" cy="500" r="235" fill="none" stroke="#38BDF8" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.5" />
    <circle cx="500" cy="500" r="145" fill="none" stroke="#818CF8" stroke-width="1.5" stroke-dasharray="4 6" opacity="0.6" />

    <!-- 60-degree Axis Construction Guidelines -->
    <line x1="500" y1="0" x2="500" y2="900" stroke="#00F2FE" stroke-width="1" stroke-dasharray="6 6" opacity="0.3" />
    <line x1="0" y1="535" x2="1000" y2="535" stroke="#00F2FE" stroke-width="1" stroke-dasharray="6 6" opacity="0.3" />
    <line x1="0" y1="635" x2="1000" y2="635" stroke="#00F2FE" stroke-width="1" stroke-dasharray="6 6" opacity="0.3" />
    
    <!-- Tangent slope lines -->
    <line x1="120" y1="840" x2="550" y2="70" stroke="#38BDF8" stroke-width="1" stroke-dasharray="3 3" opacity="0.4" />
    <line x1="880" y1="840" x2="450" y2="70" stroke="#38BDF8" stroke-width="1" stroke-dasharray="3 3" opacity="0.4" />

    <!-- The Actual Geometry with Semi-Transparency -->
    <path d="M 500 155 L 435 155 L 205 725 L 325 725 L 475 355 L 500 240 Z" fill="url(#gridGradLeft)" opacity="0.9" />
    <path d="M 500 155 L 565 155 L 795 725 L 675 725 L 525 355 L 500 240 Z" fill="url(#gridGradRight)" opacity="0.9" />
    <path d="M 290 535 L 710 535 L 645 635 L 355 635 Z" fill="url(#gridGradBridge)" opacity="0.95" />
    <polygon points="500,240 540,340 500,440 460,340" fill="#FFFFFF" opacity="0.9" />

    <!-- Vertex Anchor Points (Red Technical Crosshairs) -->
    <g fill="#F43F5E">
      <circle cx="500" cy="155" r="7" /><text x="515" y="150" font-family="monospace" font-size="18">P1 (500, 155)</text>
      <circle cx="205" cy="725" r="7" /><text x="100" y="750" font-family="monospace" font-size="18">P2 (205, 725)</text>
      <circle cx="795" cy="725" r="7" /><text x="815" y="750" font-family="monospace" font-size="18">P3 (795, 725)</text>
      <circle cx="500" cy="240" r="7" /><text x="515" y="245" font-family="monospace" font-size="18">Core &#x3C6;</text>
    </g>
  </g>

  <!-- Technical Footer Specification Callouts -->
  <g transform="translate(80, 1020)">
    <!-- Swatch 1 -->
    <rect x="0" y="0" width="48" height="48" rx="8" fill="#00F2FE" />
    <text x="60" y="22" font-family="monospace" font-size="14" font-weight="700" fill="#F8FAFC">CYBER CYAN</text>
    <text x="60" y="40" font-family="monospace" font-size="12" fill="#64748B">#00F2FE &#x2022; RGB(0, 242, 254)</text>

    <!-- Swatch 2 -->
    <rect x="280" y="0" width="48" height="48" rx="8" fill="#4F46E5" />
    <text x="340" y="22" font-family="monospace" font-size="14" font-weight="700" fill="#F8FAFC">ELECTRIC INDIGO</text>
    <text x="340" y="40" font-family="monospace" font-size="12" fill="#64748B">#4F46E5 &#x2022; RGB(79, 70, 229)</text>

    <!-- Swatch 3 -->
    <rect x="580" y="0" width="48" height="48" rx="8" fill="#9333EA" />
    <text x="640" y="22" font-family="monospace" font-size="14" font-weight="700" fill="#F8FAFC">ULTRAVIOLET</text>
    <text x="640" y="40" font-family="monospace" font-size="12" fill="#64748B">#9333EA &#x2022; RGB(147, 51, 234)</text>

    <!-- Swatch 4 -->
    <rect x="880" y="0" width="48" height="48" rx="8" fill="#090D16" stroke="#334155" stroke-width="2" />
    <text x="940" y="22" font-family="monospace" font-size="14" font-weight="700" fill="#F8FAFC">OBSIDIAN CANVAS</text>
    <text x="940" y="40" font-family="monospace" font-size="12" fill="#64748B">#090D16 &#x2022; RGB(9, 13, 22)</text>
  </g>
</svg>"""
    return svg

def build_all():
    print("Generating all Vector SVG assets...")
    
    # 1. Symbol Variants (Transparent backgrounds)
    with open("assets/vectors/aura_logo_symbol_color.svg", "w", encoding="utf-8") as f:
        f.write(get_symbol_svg("color", 1000, 1000, show_bg=False))
        
    with open("assets/vectors/aura_logo_symbol_black.svg", "w", encoding="utf-8") as f:
        f.write(get_symbol_svg("black", 1000, 1000, show_bg=False))

    with open("assets/vectors/aura_logo_symbol_white.svg", "w", encoding="utf-8") as f:
        f.write(get_symbol_svg("white", 1000, 1000, show_bg=False))

    # 2. Horizontal Lockups (Symbol + Wordmark + Tagline)
    with open("assets/vectors/aura_logo_full_color.svg", "w", encoding="utf-8") as f:
        f.write(get_horizontal_lockup_svg("color", 2400, 800, show_bg=False))

    with open("assets/vectors/aura_logo_monochrome_black.svg", "w", encoding="utf-8") as f:
        f.write(get_horizontal_lockup_svg("black", 2400, 800, show_bg=False))

    with open("assets/vectors/aura_logo_reversed_white.svg", "w", encoding="utf-8") as f:
        f.write(get_horizontal_lockup_svg("white", 2400, 800, show_bg=False))

    # 3. Vertical Stacked Lockup
    with open("assets/vectors/aura_logo_vertical_color.svg", "w", encoding="utf-8") as f:
        f.write(get_vertical_lockup_svg("color", 1200, 1400, show_bg=False))

    with open("assets/vectors/aura_logo_vertical_black.svg", "w", encoding="utf-8") as f:
        f.write(get_vertical_lockup_svg("black", 1200, 1400, show_bg=False))

    # 4. App Icon Squircle
    with open("assets/vectors/aura_logo_app_icon.svg", "w", encoding="utf-8") as f:
        f.write(get_app_icon_svg(1024, 1024))

    # 5. Technical Construction Grid Sheet
    with open("assets/vectors/aura_construction_grid.svg", "w", encoding="utf-8") as f:
        f.write(get_construction_grid_svg(1600, 1200))

    print("All vector SVGs written successfully to assets/vectors/!")

if __name__ == "__main__":
    build_all()
