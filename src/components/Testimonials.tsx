import React from 'react';
import { Star, Quote } from 'lucide-react';

const testimonials = [
  {
    quote: "Str8PositiveThinking transformed my outlook on life. Their coaching helped me overcome anxiety and build confidence in my abilities.",
    author: "Sarah J.",
    role: "Marketing Executive",
    rating: 5
  },
  {
    quote: "The community aspect of Str8PositiveThinking was a game-changer for me. Having support from others on the same journey made all the difference.",
    author: "Michael T.",
    role: "Small Business Owner",
    rating: 5
  },
  {
    quote: "I was skeptical at first, but the practical techniques they taught me have helped me manage stress and find joy in everyday moments.",
    author: "Elena K.",
    role: "Healthcare Professional",
    rating: 5
  }
];

const Testimonials = () => {
  return (
    <section id="testimonials" className="py-16 bg-gradient-to-b from-muted to-background">
      <div className="container px-4 md:px-6">
        <div className="flex flex-col items-center text-center space-y-4 mb-12">
          <div className="inline-block rounded-full bg-primary/10 px-3 py-1 text-sm font-medium text-primary">
            Success Stories
          </div>
          <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">
            Hear From Our <span className="bg-gradient-to-r from-secondary to-accent bg-clip-text text-transparent">Community</span>
          </h2>
          <p className="max-w-[700px] text-muted-foreground md:text-lg">
            Real people, real transformations. Discover how positive thinking has changed lives.
          </p>
        </div>

        <div className="grid grid-cols-1 gap-6 md:grid-cols-3">
          {testimonials.map((testimonial, index) => (
            <div 
              key={index} 
              className="flex flex-col p-8 rounded-xl bg-white border border-border shadow-sm relative overflow-hidden"
            >
              <div className="absolute -top-6 -right-6 text-primary/10">
                <Quote className="h-20 w-20" />
              </div>
              
              <div className="flex space-x-1 mb-4">
                {Array.from({ length: testimonial.rating }).map((_, i) => (
                  <Star key={i} className="h-5 w-5 fill-primary text-primary" />
                ))}
              </div>
              
              <blockquote className="text-lg font-medium mb-4 relative z-10">
                "{testimonial.quote}"
              </blockquote>
              
              <div className="mt-auto">
                <p className="font-bold">{testimonial.author}</p>
                <p className="text-sm text-muted-foreground">{testimonial.role}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Testimonials;