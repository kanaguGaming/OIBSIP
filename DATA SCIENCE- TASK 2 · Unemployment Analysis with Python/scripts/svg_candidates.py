import math

def get_svg_templates():
    # 1. Continuous Ribbon Loop A (Fluid Modernist - like Airbnb/Loop/Meta)
    # A single continuous, thick geometric ribbon forming the 'A'
    svg_ribbon = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">
  <defs>
    <linearGradient id="auragrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="40%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#6366F1" />
      <stop offset="100%" stop-color="#A855F7" />
    </linearGradient>
    <filter id="softGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="16" stdDeviation="24" flood-color="#4F46E5" flood-opacity="0.35" />
    </filter>
  </defs>
  <!-- Background for preview if needed, transparent by default -->
  <g filter="url(#softGlow)">
    <!-- Seamless continuous path: Left base -> Apex -> Right base -> Inner cross loop -->
    <path d="
      M 260 760 
      C 260 760, 420 220, 480 180
      C 500 165, 520 165, 540 180
      C 600 220, 760 760, 760 760
      C 760 760, 680 760, 650 760
      C 600 600, 560 480, 500 480
      C 440 480, 400 600, 350 760
      Z
    " fill="url(#auragrad)" />
    <!-- Dynamic Möbius Aperture Ring -->
    <circle cx="500" cy="530" r="90" stroke="url(#auragrad)" stroke-width="44" fill="none" />
  </g>
</svg>"""

    # 2. Geometric Prismatic Monogram (Precision Architectural A)
    # Inspired by Bauhaus, Dieter Rams, and high-tech spatial computing
    svg_prismatic = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">
  <defs>
    <!-- Facet Gradients -->
    <linearGradient id="facetLeft" x1="0%" y1="100%" x2="60%" y2="0%">
      <stop offset="0%" stop-color="#06B6D4" />
      <stop offset="100%" stop-color="#3B82F6" />
    </linearGradient>
    <linearGradient id="facetRight" x1="50%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3B82F6" />
      <stop offset="50%" stop-color="#6366F1" />
      <stop offset="100%" stop-color="#8B5CF6" />
    </linearGradient>
    <linearGradient id="facetBridge" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#A855F7" />
    </linearGradient>
    <linearGradient id="facetFold" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E1B4B" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#0F172A" stop-opacity="0.0" />
    </linearGradient>
  </defs>

  <g id="aura-symbol">
    <!-- Left Ascending Ribbon -->
    <path d="M 500 150 L 415 150 L 195 720 L 325 720 L 460 365 L 500 240 Z" fill="url(#facetLeft)" />
    
    <!-- Right Descending Ribbon -->
    <path d="M 500 150 L 585 150 L 805 720 L 675 720 L 540 365 L 500 240 Z" fill="url(#facetRight)" />
    
    <!-- Central Horizon Möbius Fold -->
    <path d="M 295 530 L 705 530 L 635 635 L 365 635 Z" fill="url(#facetBridge)" />

    <!-- Negative Space Center Counterform -->
    <!-- Triangle formed by (500, 310), (410, 530), (590, 530) -->
    
    <!-- Ambient Orbital Spark Core (The "Aura") -->
    <circle cx="500" cy="445" r="32" fill="#FFFFFF" opacity="0.95" />
    
    <!-- Shadow fold across right connection -->
    <polygon points="590,530 635,635 550,580" fill="url(#facetFold)" />
  </g>
</svg>"""

    # 3. Modern Pure Line / Infinite Vector A (Golden Ratio, Ultra Minimalist)
    svg_minimal_line = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000" width="1000" height="1000">
  <defs>
    <linearGradient id="lineGrad" x1="0%" y1="100%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" />
      <stop offset="35%" stop-color="#38BDF8" />
      <stop offset="70%" stop-color="#6366F1" />
      <stop offset="100%" stop-color="#C084FC" />
    </linearGradient>
    <filter id="glowEffect" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="16" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <g filter="url(#glowEffect)">
    <!-- Outer Chevron Apex -->
    <path d="M 230 750 L 500 190 L 770 750" 
          stroke="url(#lineGrad)" 
          stroke-width="72" 
          stroke-linecap="round" 
          stroke-linejoin="round" 
          fill="none" />
    
    <!-- Ambient Halo Loop (Crossbar & Orbit) -->
    <!-- Intersecting circle/ellipse centered at (500, 520) -->
    <ellipse cx="500" cy="520" rx="210" ry="110" 
             stroke="url(#lineGrad)" 
             stroke-width="64" 
             fill="none" />
  </g>
</svg>"""

    return {
        "ribbon": svg_ribbon,
        "prismatic": svg_prismatic,
        "minimal_line": svg_minimal_line
    }

print("SVG templates defined.")
