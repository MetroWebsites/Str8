import React from "react";
import { Brain, Heart, Sparkles } from "lucide-react";

const Footer = () => {
  return (
    <footer className="pt-20 pb-10 border-t border-primary/10 relative overflow-hidden">
      {/* Background elements */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute bottom-0 left-1/4 w-64 h-64 bg-primary/5 rounded-full blur-[100px]"></div>
        <div className="absolute bottom-1/4 right-1/3 w-64 h-64 bg-secondary/5 rounded-full blur-[100px]"></div>
      </div>
      
      <div className="container mx-auto px-4">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-12 mb-16">
          <div className="lg:col-span-2">
            <div className="flex items-center gap-2 mb-6">
              <div className="relative">
                <div className="absolute inset-0 rounded-full blur-sm bg-primary/50"></div>
                <div className="relative flex items-center justify-center w-10 h-10 rounded-full bg-background border border-primary">
                  <Brain className="h-5 w-5 text-primary" />
                </div>
              </div>
              <div>
                <div className="font-bold text-xl">
                  <span className="bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">Str8Positive</span>
                </div>
                <div className="text-xs text-muted-foreground">Transform Your Mindset</div>
              </div>
            </div>
            
            <p className="text-sm text-muted-foreground mb-6 max-w-md">
              Str8Positive is dedicated to helping individuals transform their lives through the power of positive thinking, providing tools, resources and community support.
            </p>
            
            <div className="flex space-x-4">
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <span className="sr-only">Facebook</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <span className="sr-only">Instagram</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <span className="sr-only">Twitter</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"/></svg>
              </a>
              <a href="#" className="text-muted-foreground hover:text-primary transition-colors">
                <span className="sr-only">LinkedIn</span>
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/></svg>
              </a>
            </div>
          </div>
          
          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider mb-4">Company</h3>
            <ul className="space-y-3">
              <li><a href="#about" className="text-sm text-muted-foreground hover:text-primary transition-colors">About</a></li>
              <li><a href="#" className="text-sm text-muted-foreground hover:text-primary transition-colors">Careers</a></li>
              <li><a href="#" className="text-sm text-muted-foreground hover:text-primary transition-colors">Press</a></li>
              <li><a href="#" className="text-sm text-muted-foreground hover:text-primary transition-colors">Blog</a></li>
            </ul>
          </div>
          
          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider mb-4">Services</h3>
            <ul className="space-y-3">
              <li><a href="#services" className="text-sm text-muted-foreground hover:text-primary transition-colors">Coaching</a></li>
              <li><a href="#services" className="text-sm text-muted-foreground hover:text-primary transition-colors">Courses</a></li>
              <li><a href="#services" className="text-sm text-muted-foreground hover:text-primary transition-colors">Community</a></li>
              <li><a href="#services" className="text-sm text-muted-foreground hover:text-primary transition-colors">Resources</a></li>
            </ul>
          </div>
          
          <div>
            <h3 className="text-sm font-semibold uppercase tracking-wider mb-4">Legal</h3>
            <ul className="space-y-3">
              <li><a href="#" className="text-sm text-muted-foreground hover:text-primary transition-colors">Privacy</a></li>
              <li><a href="#" className="text-sm text-muted-foreground hover:text-primary transition-colors">Terms</a></li>
              <li><a href="#" className="text-sm text-muted-foreground hover:text-primary transition-colors">Cookies</a></li>
              <li><a href="#" className="text-sm text-muted-foreground hover:text-primary transition-colors">Licenses</a></li>
            </ul>
          </div>
        </div>
        
        <div className="border-t border-primary/10 pt-8 flex flex-col md:flex-row justify-between items-center">
          <p className="text-sm text-muted-foreground mb-4 md:mb-0">
            &copy; {new Date().getFullYear()} Str8Positive. All rights reserved.
          </p>
          
          <div className="flex items-center gap-2">
            <span className="text-sm text-muted-foreground">Built with</span>
            <Heart className="h-4 w-4 text-primary" />
            <a
              href="https://new.website"
              target="_blank"
              rel="noreferrer"
              className="text-sm text-primary hover:text-primary/80 transition-colors font-medium"
            >
              new.website
            </a>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;