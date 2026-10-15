import os
import math

# Let's create an elegant, mathematically sound geometric mark
# We will create the SVG generators for AURA

def create_aura_mark_svg(variant="color", width=1000, height=1000):
    """
    Variants:
    - 'color': Vibrant cyber-indigo and ultraviolet gradients with luminous depth
    - 'black': Pure monochrome #09090b with negative space gaps (ideal for single-color print, vinyl, laser etch)
    - 'white': Pure reversed #ffffff with negative space gaps (ideal for dark mode, apparel, stamps)
    """
    
    # Mathematical Coordinates for the 'Aura Prism' (Möbius-inspired architectural 'A')
    # Built using 3 interlocking geometric ribbons with golden ratio bevels:
    # Ribbon A: The Left Apex Ascent (Foundation to Peak)
    # Ribbon B: The Right Descent & Horizon Turn (Peak to Lower Base)
    # Ribbon C: The Möbius Infinity Crossbar (Connecting Base to Center Core)
    
    # Gradients & Colors
    defs = ""
    if variant == "color":
        defs = """
    <defs>
      <!-- Gradient 1: Left Ascent (Cyan to Royal Blue) -->
      <linearGradient id="gradLeft" x1="0%" y1="100%" x2="50%" y2="0%">
        <stop offset="0%" stop-color="#00F2FE" />
        <stop offset="40%" stop-color="#38BDF8" />
        <stop offset="100%" stop-color="#6366F1" />
      </linearGradient>

      <!-- Gradient 2: Right Descent (Royal Blue to Deep Indigo Violet) -->
      <linearGradient id="gradRight" x1="50%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#6366F1" />
        <stop offset="60%" stop-color="#8B5CF6" />
        <stop offset="100%" stop-color="#4F46E5" />
      </linearGradient>

      <!-- Gradient 3: Möbius Crossbar (Ultraviolet to Vibrant Magenta to Sky Cyan) -->
      <linearGradient id="gradCross" x1="0%" y1="50%" x2="100%" y2="50%">
        <stop offset="0%" stop-color="#A855F7" />
        <stop offset="50%" stop-color="#6366F1" />
        <stop offset="100%" stop-color="#38BDF8" />
      </linearGradient>

      <!-- Inner Core Shadow for Optical Depth -->
      <linearGradient id="coreShadow" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0F172A" stop-opacity="0.28" />
        <stop offset="100%" stop-color="#0F172A" stop-opacity="0.0" />
      </linearGradient>

      <!-- Subtle Ambient Glow -->
      <filter id="ambientGlow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="35" result="blur" />
        <feComposite in="SourceGraphic" in2="blur" operator="over" />
      </filter>
    </defs>
    """
        fill_left = "url(#gradLeft)"
        fill_right = "url(#gradRight)"
        fill_cross = "url(#gradCross)"
        fill_cap = "#38BDF8"
        shadow_style = 'fill="url(#coreShadow)"'
    elif variant == "black":
        fill_left = "#09090B"
        fill_right = "#09090B"
        fill_cross = "#09090B"
        fill_cap = "#09090B"
        shadow_style = 'display="none"'
    elif variant == "white":
        fill_left = "#FFFFFF"
        fill_right = "#FFFFFF"
        fill_cross = "#FFFFFF"
        fill_cap = "#FFFFFF"
        shadow_style = 'display="none"'

    # Polygons / Paths
    # Precision coordinates calibrated on a 1000x1000 viewport
    # Apex at (500, 160)
    # Left base at (230, 720)
    # Right base at (770, 720)
    # Optical gap between ribbons for monochrome printing clarity = 12px
    
    gap = 14 if variant in ["black", "white"] else 6

    # Ribbon 1: Left Pillar & Outer Apex
    # Ascends from left base to apex, folds cleanly
    path_left = f"""
      <path d="
        M 230,720 
        L 345,720 
        L 485,345 
        L 485,270 
        L 500,165 
        L 455,165 
        L 230,720 Z
      " fill="{fill_left}" />
    """

    # Let's construct a cleaner, more sculptural continuous geometric loop
    # Let's use a 4-part impossible prism ribbon that mirrors modern luxury tech
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="100%">
    {defs}
    <g id="aura-symbol">
      <!-- Facet 1: Ascending Left Ribbon -->
      <path d="M 500 160 L 450 160 L 220 710 L 330 710 L 485 320 Z" fill="{fill_left}" />
      
      <!-- Facet 2: Descending Right Ribbon -->
      <path d="M 500 160 L 550 160 L 780 710 L 670 710 L 515 320 Z" fill="{fill_right}" />
      
      <!-- Facet 3: Möbius Crossbar Bridge (Left connection curving across) -->
      <path d="M 315 540 L 400 330 L 525 330 L 440 540 Z" fill="{fill_cross}" opacity="0.95" />
      
      <!-- Facet 4: Horizontal Horizon Shelf & Apex Loop -->
      <path d="M 370 540 L 630 540 L 675 640 L 325 640 Z" fill="{fill_left if variant != 'color' else 'url(#gradCross)'}" />

      <!-- Dimensional Interlock Shadow (Color only) -->
      <path d="M 440 540 L 525 330 L 545 375 L 470 540 Z" {shadow_style} />
    </g>
</svg>"""
    return svg_content

print("Script template ready")
