import React from "react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Sparkles, ArrowRight } from "lucide-react";

const CtaSection = () => {
  return (
    <section className="py-20 relative overflow-hidden">
      <div className="container mx-auto px-4">
        <div className="relative">
          {/* Glow effects */}
          <div className="absolute -inset-4 bg-gradient-to-r from-primary/30 via-secondary/30 to-accent/30 rounded-3xl blur-xl"></div>
          
          <div className="relative rounded-2xl overflow-hidden">
            {/* Background with subtle animation */}
            <div className="absolute inset-0 bg-gradient-to-br from-primary/20 via-secondary/20 to-accent/20 opacity-70"></div>
            
            {/* Animated background elements */}
            <div className="absolute top-0 left-0 w-full h-full overflow-hidden">
              <div className="absolute top-1/4 left-1/4 w-64 h-64 rounded-full bg-primary/20 blur-3xl animate-pulse"></div>
              <div className="absolute bottom-1/4 right-1/4 w-64 h-64 rounded-full bg-secondary/20 blur-3xl animate-pulse" style={{animationDelay: "1s"}}></div>
              <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-64 h-64 rounded-full bg-accent/20 blur-3xl animate-pulse" style={{animationDelay: "2s"}}></div>
            </div>
            
            <div className="relative p-10 md:p-16 backdrop-blur-sm border border-primary/30">
              <div className="max-w-3xl mx-auto text-center">
                <Badge variant="neon" className="mb-6">
                  <Sparkles className="h-3.5 w-3.5 mr-1" />
                  Limited Time Offer
                </Badge>
                
                <h2 className="text-3xl md:text-4xl lg:text-5xl font-bold mb-6 leading-tight">
                  Start Your <span className="bg-gradient-to-r from-primary via-secondary to-accent bg-clip-text text-transparent">Positive Thinking</span> Journey Today
                </h2>
                
                <p className="text-lg mb-8 text-muted-foreground">
                  Join thousands of others who have transformed their lives through the power of positive thinking.
                  Get access to our exclusive resources, coaching, and supportive community.
                </p>
                
                <div className="flex flex-col sm:flex-row gap-4 justify-center">
                  <div className="relative group">
                    <div className="absolute -inset-1 rounded-lg blur-md bg-gradient-to-r from-primary to-secondary opacity-70 group-hover:opacity-100 transition-opacity"></div>
                    <Button className="relative w-full text-lg px-8 py-6 bg-gradient-to-r from-primary to-secondary hover:from-primary/90 hover:to-secondary/90">
                      Get Started Now
                      <ArrowRight className="ml-2 h-5 w-5" />
                    </Button>
                  </div>
                  
                  <Button variant="outline" className="w-full sm:w-auto text-lg px-8 py-6 border-white/20 hover:bg-white/10 text-white">
                    Learn More
                  </Button>
                </div>
                
                <div className="mt-8 text-sm text-muted-foreground">
                  No credit card required • 7-day free trial • Cancel anytime
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CtaSection;