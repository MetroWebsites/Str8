import React, { useState } from "react";
import { Brain, Menu, X, Sparkles, WandSparkles } from "lucide-react";
import { Button } from "@/components/ui/button";

const Navigation = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  return (
    <header className="fixed top-0 left-0 right-0 z-50 py-4 backdrop-blur-md bg-background/60 border-b border-primary/20">
      <div className="container flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="relative">
            <div className="absolute -inset-1 rounded-full blur-md bg-primary/50"></div>
            <div className="relative flex items-center justify-center w-10 h-10 rounded-full bg-background border border-primary">
              <Brain className="h-5 w-5 text-primary" />
            </div>
          </div>
          <a href="/" className="font-bold text-xl tracking-tight">
            <span className="bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">Str8Positive</span>
          </a>
        </div>

        {/* Desktop Navigation */}
        <nav className="hidden md:flex items-center gap-6">
          <a href="#about" className="text-sm font-medium hover:text-primary transition-colors relative group">
            About
            <span className="absolute left-0 right-0 bottom-0 h-px bg-primary transform scale-x-0 group-hover:scale-x-100 transition-transform"></span>
          </a>
          <a href="#services" className="text-sm font-medium hover:text-primary transition-colors relative group">
            Services
            <span className="absolute left-0 right-0 bottom-0 h-px bg-primary transform scale-x-0 group-hover:scale-x-100 transition-transform"></span>
          </a>
          <a href="#testimonials" className="text-sm font-medium hover:text-primary transition-colors relative group">
            Testimonials
            <span className="absolute left-0 right-0 bottom-0 h-px bg-primary transform scale-x-0 group-hover:scale-x-100 transition-transform"></span>
          </a>
          <a href="#contact" className="relative">
            <div className="absolute -inset-[2px] rounded-lg blur-md bg-gradient-to-r from-primary to-secondary opacity-70 group-hover:opacity-100 transition-opacity"></div>
            <Button 
              variant="outline"
              className="relative border border-primary/50 hover:border-primary/80 text-foreground bg-background hover:text-primary"
            >
              <Sparkles className="mr-2 h-4 w-4" />
              Get Started
            </Button>
          </a>
        </nav>

        {/* Mobile Menu Toggle */}
        <Button 
          variant="ghost" 
          size="icon"
          onClick={() => setIsMenuOpen(!isMenuOpen)}
          className="md:hidden"
        >
          {isMenuOpen ? (
            <X className="h-6 w-6" />
          ) : (
            <Menu className="h-6 w-6" />
          )}
        </Button>
      </div>

      {/* Mobile Navigation */}
      {isMenuOpen && (
        <div className="fixed inset-0 top-[73px] z-40 bg-background border-t border-primary/20 md:hidden">
          <nav className="container flex flex-col gap-4 py-8">
            <a 
              href="#about" 
              className="text-lg font-medium py-4 border-b border-muted flex items-center"
              onClick={() => setIsMenuOpen(false)}
            >
              About
            </a>
            <a 
              href="#services" 
              className="text-lg font-medium py-4 border-b border-muted flex items-center"
              onClick={() => setIsMenuOpen(false)}
            >
              Services
            </a>
            <a 
              href="#testimonials" 
              className="text-lg font-medium py-4 border-b border-muted flex items-center"
              onClick={() => setIsMenuOpen(false)}
            >
              Testimonials
            </a>
            <a 
              href="#contact" 
              className="mt-4 w-full"
              onClick={() => setIsMenuOpen(false)}
            >
              <Button className="w-full">
                <WandSparkles className="mr-2 h-5 w-5" />
                Get Started
              </Button>
            </a>
          </nav>
        </div>
      )}
    </header>
  );
};

export default Navigation;