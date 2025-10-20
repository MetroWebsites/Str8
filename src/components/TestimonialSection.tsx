import React from "react";
import { Badge } from "@/components/ui/badge";
import { Star, Quote, Sparkles } from "lucide-react";

const testimonials = [
  {
    quote: "Str8Positive transformed my outlook on life. Their coaching helped me overcome anxiety and build confidence in my abilities.",
    author: "Sarah J.",
    role: "Marketing Executive",
    rating: 5,
    gradient: "from-primary/20 via-accent/10 to-secondary/20"
  },
  {
    quote: "The community aspect of Str8Positive was a game-changer for me. Having support from others on the same journey made all the difference.",
    author: "Michael T.",
    role: "Small Business Owner",
    rating: 5,
    gradient: "from-secondary/20 via-primary/10 to-accent/20"
  },
  {
    quote: "I was skeptical at first, but the practical techniques they taught me have helped me manage stress and find joy in everyday moments.",
    author: "Elena K.",
    role: "Healthcare Professional",
    rating: 5,
    gradient: "from-accent/20 via-secondary/10 to-primary/20"
  }
];

const TestimonialSection = () => {
  return (
    <section id="testimonials" className="py-20 relative overflow-hidden">
      {/* Background elements */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute top-20 right-1/3 w-72 h-72 bg-accent/10 rounded-full blur-[100px]"></div>
        <div className="absolute bottom-20 left-1/3 w-72 h-72 bg-primary/10 rounded-full blur-[100px]"></div>
      </div>
      
      <div className="container mx-auto px-4">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <Badge variant="ghost" className="mb-4">
            Success Stories
          </Badge>
          <h2 className="text-3xl md:text-4xl font-bold mb-6">
            Hear From Our <span className="bg-gradient-to-r from-secondary to-accent bg-clip-text text-transparent">Community</span>
          </h2>
          <p className="text-muted-foreground">
            Real people, real transformations. Discover how positive thinking has changed lives.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {testimonials.map((testimonial, index) => (
            <div key={index} className="relative group">
              <div className={`absolute -inset-2 rounded-xl bg-gradient-to-r ${testimonial.gradient} opacity-40 group-hover:opacity-70 blur-lg transition-opacity duration-300`}></div>
              
              <div className="relative bg-card border border-primary/10 rounded-xl p-8 h-full backdrop-blur-sm transition-all duration-300 hover:border-primary/30">
                <div className="absolute -top-4 -right-4 text-primary/10 opacity-50">
                  <Quote className="h-20 w-20" />
                </div>
                
                <div className="flex space-x-1 mb-4">
                  {Array.from({ length: testimonial.rating }).map((_, i) => (
                    <Star key={i} className="h-5 w-5 text-primary fill-primary" />
                  ))}
                </div>
                
                <blockquote className="relative text-lg font-medium mb-6 z-10">
                  "{testimonial.quote}"
                </blockquote>
                
                <div className="flex items-center mt-auto pt-6 border-t border-primary/10">
                  {/* Avatar placeholder with glow effect */}
                  <div className="relative mr-4">
                    <div className="absolute inset-0 rounded-full bg-gradient-to-r from-primary/50 to-secondary/50 blur-sm"></div>
                    <div className="relative w-10 h-10 rounded-full bg-gradient-to-r from-primary to-secondary flex items-center justify-center">
                      <span className="text-white font-bold text-sm">{testimonial.author.charAt(0)}</span>
                    </div>
                  </div>
                  
                  <div>
                    <p className="font-bold text-sm">{testimonial.author}</p>
                    <p className="text-xs text-muted-foreground">{testimonial.role}</p>
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
        
        <div className="mt-16 text-center">
          <div className="inline-flex items-center px-6 py-3 rounded-full bg-muted text-sm">
            <Sparkles className="h-4 w-4 text-primary mr-2" />
            Join thousands of others who have transformed their lives
          </div>
        </div>
      </div>
    </section>
  );
};

export default TestimonialSection;