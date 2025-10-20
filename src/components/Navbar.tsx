import React from 'react';
import { buttonVariants } from "@/components/ui/button";
import { Sun, Brain, Heart, Sparkles } from 'lucide-react';

const Navbar = () => {
  return (
    <header className="bg-white/95 supports-[backdrop-filter]:bg-white/60 sticky top-0 z-50 w-full border-b border-primary/20 backdrop-blur shadow-sm">
      <div className="container flex h-20 items-center space-x-4 sm:justify-between sm:space-x-0">
        <div className="flex items-center gap-3">
          <Sun className="h-8 w-8 text-primary" />
          <a href="/" className="flex flex-col">
            <span className="text-xl font-bold tracking-tight bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">
              Str8PositiveThinking
            </span>
            <span className="text-xs text-muted-foreground tracking-wide">Elevate Your Mind, Transform Your Life</span>
          </a>
        </div>
        <div className="flex flex-1 items-center justify-end space-x-4">
          <nav className="flex items-center space-x-2">
            <a
              href="#about"
              className={buttonVariants({ variant: 'ghost', size: 'sm', className: 'text-foreground font-medium' })}
            >
              About
            </a>
            <a
              href="#services"
              className={buttonVariants({ variant: 'ghost', size: 'sm', className: 'text-foreground font-medium' })}
            >
              Services
            </a>
            <a
              href="#testimonials"
              className={buttonVariants({ variant: 'ghost', size: 'sm', className: 'text-foreground font-medium' })}
            >
              Testimonials
            </a>
            <a
              href="#contact"
              className={buttonVariants({ 
                variant: 'default', 
                size: 'sm', 
                className: 'bg-primary text-primary-foreground hover:bg-primary/90 ml-2 font-medium'
              })}
            >
              Get Started
            </a>
          </nav>
        </div>
      </div>
    </header>
  );
};

export default Navbar;