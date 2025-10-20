import React from 'react';
import { buttonVariants } from "@/components/ui/button";
import { Sun, Brain, Heart, Sparkles, ArrowRight } from 'lucide-react';

const Hero = () => {
  return (
    <section className="relative py-20 overflow-hidden">
      {/* Background decorations */}
      <div className="absolute -top-24 -right-24 w-64 h-64 bg-primary/10 rounded-full blur-3xl"></div>
      <div className="absolute top-1/2 -left-24 w-64 h-64 bg-secondary/10 rounded-full blur-3xl"></div>
      <div className="absolute bottom-0 right-1/3 w-64 h-64 bg-accent/10 rounded-full blur-3xl"></div>
      
      <div className="container px-4 md:px-6">
        <div className="grid gap-6 lg:grid-cols-[1fr_400px] lg:gap-12 xl:grid-cols-[1fr_600px]">
          <div className="flex flex-col justify-center space-y-8">
            <div className="space-y-6">
              <div className="inline-block rounded-full bg-primary/10 px-3 py-1 text-sm font-medium text-primary">
                <span className="flex items-center gap-1">
                  <Sparkles className="h-4 w-4" /> Transform Your Mindset Today
                </span>
              </div>
              <h1 className="text-4xl font-extrabold tracking-tight sm:text-5xl md:text-6xl lg:text-7xl">
                Unlock Your <span className="bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">Positive</span> Potential
              </h1>
              <p className="max-w-[700px] text-lg text-muted-foreground md:text-xl">
                Discover the power of positive thinking and transform your life with our proven techniques, coaching, and community support.
              </p>
            </div>
            <div className="flex flex-col gap-4 min-[400px]:flex-row">
              <a
                href="#services"
                className={buttonVariants({
                  size: "lg",
                  className: "bg-primary text-primary-foreground hover:bg-primary/90 font-medium"
                })}
              >
                <span>Explore Services</span>
                <ArrowRight className="ml-2 h-4 w-4" />
              </a>
              <a
                href="#about"
                className={buttonVariants({
                  variant: "outline",
                  size: "lg",
                  className: "font-medium"
                })}
              >
                Learn More
              </a>
            </div>
            <div className="flex items-center gap-4 text-sm">
              <div className="flex -space-x-2">
                <div className="inline-flex h-8 w-8 items-center justify-center rounded-full bg-primary">
                  <Heart className="h-4 w-4 text-white" />
                </div>
                <div className="inline-flex h-8 w-8 items-center justify-center rounded-full bg-secondary">
                  <Brain className="h-4 w-4 text-white" />
                </div>
                <div className="inline-flex h-8 w-8 items-center justify-center rounded-full bg-accent">
                  <Sun className="h-4 w-4 text-white" />
                </div>
              </div>
              <div className="text-muted-foreground">
                <span className="font-medium">Trusted by 10,000+</span> people worldwide
              </div>
            </div>
          </div>
          <div className="flex items-center justify-center">
            <div className="relative h-[400px] w-full overflow-hidden rounded-xl bg-gradient-to-br from-primary/20 via-secondary/20 to-accent/20 p-10 shadow-lg">
              <div className="absolute inset-0 flex flex-col items-center justify-center p-6 text-center">
                <div className="rounded-full bg-white/90 p-4 shadow-lg">
                  <Sun className="h-12 w-12 text-primary" />
                </div>
                <h3 className="mt-6 text-xl font-bold">Daily Positive Affirmations</h3>
                <div className="mt-4 space-y-4">
                  <div className="rounded-lg bg-white/90 px-4 py-2 font-medium shadow-sm">
                    "I am capable of amazing things"
                  </div>
                  <div className="rounded-lg bg-white/90 px-4 py-2 font-medium shadow-sm">
                    "My potential is limitless"
                  </div>
                  <div className="rounded-lg bg-white/90 px-4 py-2 font-medium shadow-sm">
                    "I attract positivity into my life"
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;