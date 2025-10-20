import React from 'react';
import { buttonVariants } from "@/components/ui/button";
import { Sparkles, ArrowRight } from 'lucide-react';

const CallToAction = () => {
  return (
    <section className="py-16">
      <div className="container px-4 md:px-6">
        <div className="rounded-3xl bg-gradient-to-br from-primary/90 via-primary to-secondary p-8 md:p-10 lg:p-16 relative overflow-hidden">
          {/* Background decorations */}
          <div className="absolute top-0 right-0 w-64 h-64 bg-white/10 rounded-full translate-x-1/2 -translate-y-1/2 blur-3xl"></div>
          <div className="absolute bottom-0 left-0 w-64 h-64 bg-white/10 rounded-full -translate-x-1/2 translate-y-1/2 blur-3xl"></div>
          
          <div className="relative z-10 flex flex-col items-center text-center space-y-8 max-w-3xl mx-auto">
            <div className="inline-block rounded-full bg-white/20 backdrop-blur-sm px-3 py-1 text-sm font-medium text-white">
              <span className="flex items-center gap-1">
                <Sparkles className="h-4 w-4" /> Limited Time Offer
              </span>
            </div>
            
            <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight lg:text-5xl/tight text-white">
              Start Your Positive Thinking Journey Today
            </h2>
            
            <p className="text-white/90 text-lg md:text-xl">
              Join thousands of others who have transformed their lives through the power of positive thinking. 
              Get access to our exclusive resources, coaching, and supportive community.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-4">
              <a
                href="#contact"
                className={buttonVariants({
                  size: "lg",
                  className: "bg-white text-primary hover:bg-white/90 font-medium"
                })}
              >
                <span>Get Started Now</span>
                <ArrowRight className="ml-2 h-4 w-4" />
              </a>
              
              <a
                href="#services"
                className={buttonVariants({
                  variant: "outline",
                  size: "lg",
                  className: "border-white text-white hover:bg-white/10 font-medium"
                })}
              >
                Learn More
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default CallToAction;