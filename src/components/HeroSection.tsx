import React from "react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Sparkles, BrainCog, ArrowRight } from "lucide-react";

const HeroSection = () => {
  return (
    <section className="pt-32 pb-20 overflow-hidden relative">
      {/* Background elements */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute top-20 left-1/4 w-72 h-72 bg-primary/20 rounded-full blur-[100px]"></div>
        <div className="absolute bottom-20 right-1/4 w-72 h-72 bg-secondary/20 rounded-full blur-[100px]"></div>
        <div className="absolute top-40 right-1/3 w-72 h-72 bg-accent/20 rounded-full blur-[100px]"></div>
      </div>

      <div className="container mx-auto px-4 relative">
        <Badge variant="ghost" className="mb-6 mx-auto md:mx-0 flex items-center gap-1 justify-center md:justify-start">
          <Sparkles className="h-3.5 w-3.5" />
          <span>Transform Your Mindset</span>
        </Badge>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <div className="text-center md:text-left">
            <h1 className="text-4xl md:text-5xl lg:text-6xl xl:text-7xl font-bold tracking-tight mb-6 leading-tight">
              <span className="block">Unlock Your</span>
              <span className="bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">Positive Potential</span>
            </h1>

            <p className="text-lg mb-8 text-muted-foreground max-w-xl mx-auto md:mx-0">
              Discover the power of positive thinking and transform your life with our proven techniques, coaching, and supportive community.
            </p>

            <div className="flex flex-col sm:flex-row gap-4 justify-center md:justify-start">
              <div className="relative group">
                <div className="absolute -inset-1 rounded-lg blur-md bg-gradient-to-r from-primary to-secondary opacity-70 group-hover:opacity-100 transition-opacity"></div>
                <Button className="relative w-full text-lg px-8 py-6 bg-gradient-to-r from-primary to-secondary hover:from-primary/90 hover:to-secondary/90">
                  Get Started
                  <ArrowRight className="ml-2 h-5 w-5" />
                </Button>
              </div>
              
              <Button variant="outline" className="w-full sm:w-auto text-lg px-8 py-6 border-primary/50 hover:border-primary">
                Learn More
              </Button>
            </div>
          </div>

          {/* 3D-like card interface */}
          <div className="relative">
            <div className="absolute -inset-4 bg-gradient-to-r from-primary/20 via-secondary/20 to-accent/20 rounded-2xl blur-lg"></div>
            
            <div className="relative bg-card p-8 rounded-xl border border-primary/20 backdrop-blur-sm">
              <div className="relative space-y-8">
                <div className="flex items-center gap-4">
                  <div className="flex items-center justify-center w-14 h-14 rounded-xl bg-primary/10 backdrop-blur-sm border border-primary/30">
                    <BrainCog className="h-7 w-7 text-primary" />
                  </div>
                  <div>
                    <h3 className="text-xl font-bold">Mindset Transformation</h3>
                    <p className="text-sm text-muted-foreground">Rewire your thinking patterns</p>
                  </div>
                </div>
                
                <div className="space-y-4">
                  <div className="bg-muted p-4 rounded-lg relative overflow-hidden group">
                    <div className="absolute inset-0 bg-gradient-to-r from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <p className="relative text-sm font-medium">"I am capable of achieving my goals and dreams."</p>
                  </div>
                  
                  <div className="bg-muted p-4 rounded-lg relative overflow-hidden group">
                    <div className="absolute inset-0 bg-gradient-to-r from-secondary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <p className="relative text-sm font-medium">"Every day I'm growing stronger and more positive."</p>
                  </div>
                  
                  <div className="bg-muted p-4 rounded-lg relative overflow-hidden group">
                    <div className="absolute inset-0 bg-gradient-to-r from-accent/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                    <p className="relative text-sm font-medium">"I attract abundance and positivity into my life."</p>
                  </div>
                </div>
                
                <div className="pt-2">
                  <div className="flex items-center justify-between">
                    <p className="text-sm text-muted-foreground">Daily affirmations</p>
                    <Badge variant="neon">
                      <Sparkles className="h-3 w-3 mr-1" />
                      Powerful
                    </Badge>
                  </div>
                </div>
              </div>
            </div>
            
            {/* Decorative elements */}
            <div className="absolute -top-6 -right-6 w-12 h-12 bg-primary/30 rounded-full blur-lg"></div>
            <div className="absolute -bottom-6 -left-6 w-12 h-12 bg-secondary/30 rounded-full blur-lg"></div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;