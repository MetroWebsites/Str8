import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Send, Sparkles, Phone, Mail, MapPin } from "lucide-react";

const ContactSection = () => {
  const defaultFormData = {name: "", email: "", message: "", form_name: "Positive Thinking Inquiry"};
  const [formData, setFormData] = useState(defaultFormData);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitStatus, setSubmitStatus] = useState<"success" | "error" | null>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    setSubmitStatus(null);

    try {
      const response = await fetch("https://api.new.website/api/submit-form/", {
        method: "POST",
        headers: {
          "Content-Type": "multipart/form-data",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setSubmitStatus("success");
        setFormData(defaultFormData);
      } else {
        setSubmitStatus("error");
      }
    } catch (error) {
      setSubmitStatus("error");
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <section id="contact" className="py-20 relative overflow-hidden">
      {/* Background elements */}
      <div className="absolute inset-0 -z-10">
        <div className="absolute top-20 left-1/3 w-72 h-72 bg-secondary/10 rounded-full blur-[100px]"></div>
        <div className="absolute bottom-40 right-1/4 w-72 h-72 bg-primary/10 rounded-full blur-[100px]"></div>
      </div>
      
      <div className="container mx-auto px-4">
        <div className="text-center max-w-3xl mx-auto mb-16">
          <Badge variant="ghost" className="mb-4">
            <Sparkles className="h-3.5 w-3.5 mr-1" />
            Get In Touch
          </Badge>
          <h2 className="text-3xl md:text-4xl font-bold mb-6">
            Start Your <span className="bg-gradient-to-r from-primary to-secondary bg-clip-text text-transparent">Positive Journey</span> Today
          </h2>
          <p className="text-muted-foreground">
            Have questions? Ready to transform your mindset? Fill out the form below and we'll get back to you shortly.
          </p>
        </div>
        
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10">
          <div className="relative">
            <div className="absolute -inset-4 bg-gradient-to-r from-primary/20 via-secondary/20 to-accent/20 rounded-2xl blur-lg"></div>
            
            <div className="relative bg-card p-8 rounded-xl border border-primary/20 h-full backdrop-blur-sm">
              <div className="space-y-8">
                <div>
                  <h3 className="text-xl font-bold mb-3">Contact Information</h3>
                  <p className="text-muted-foreground">
                    We're here to help you on your journey to positive thinking.
                  </p>
                </div>
                
                <div className="space-y-6">
                  <div className="flex items-center gap-4">
                    <div className="relative flex-shrink-0">
                      <div className="absolute inset-0 rounded-full bg-primary/30 blur-sm"></div>
                      <div className="relative p-3 rounded-full">
                        <Phone className="h-5 w-5 text-primary" />
                      </div>
                    </div>
                    <div>
                      <p className="text-sm font-medium">Phone</p>
                      <p className="text-sm text-muted-foreground">(123) 456-7890</p>
                    </div>
                  </div>
                  
                  <div className="flex items-center gap-4">
                    <div className="relative flex-shrink-0">
                      <div className="absolute inset-0 rounded-full bg-secondary/30 blur-sm"></div>
                      <div className="relative p-3 rounded-full">
                        <Mail className="h-5 w-5 text-secondary" />
                      </div>
                    </div>
                    <div>
                      <p className="text-sm font-medium">Email</p>
                      <p className="text-sm text-muted-foreground">hello@str8positive.com</p>
                    </div>
                  </div>
                  
                  <div className="flex items-center gap-4">
                    <div className="relative flex-shrink-0">
                      <div className="absolute inset-0 rounded-full bg-accent/30 blur-sm"></div>
                      <div className="relative p-3 rounded-full">
                        <MapPin className="h-5 w-5 text-accent" />
                      </div>
                    </div>
                    <div>
                      <p className="text-sm font-medium">Location</p>
                      <p className="text-sm text-muted-foreground">123 Positive Street, Mindful City, ST 12345</p>
                    </div>
                  </div>
                </div>
                
                <div className="pt-8 border-t border-primary/10">
                  <div className="flex items-center gap-4">
                    <a href="#" className="text-muted-foreground hover:text-foreground transition-colors">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
                    </a>
                    <a href="#" className="text-muted-foreground hover:text-foreground transition-colors">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect width="20" height="20" x="2" y="2" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" x2="17.51" y1="6.5" y2="6.5"/></svg>
                    </a>
                    <a href="#" className="text-muted-foreground hover:text-foreground transition-colors">
                      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"/></svg>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <div className="relative">
            <div className="absolute -inset-4 bg-gradient-to-r from-primary/10 via-secondary/10 to-accent/10 rounded-2xl blur-lg"></div>
            
            <form 
              onSubmit={handleSubmit}
              className="relative bg-card p-8 rounded-xl border border-primary/20 backdrop-blur-sm space-y-6"
            >
              <div>
                <label htmlFor="name" className="block text-sm font-medium mb-2">
                  Name
                </label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  value={formData.name}
                  onChange={handleInputChange}
                  required
                  className="w-full px-4 py-3 bg-muted/50 border border-primary/10 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50"
                  placeholder="Your name"
                />
              </div>

              <div>
                <label htmlFor="email" className="block text-sm font-medium mb-2">
                  Email
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleInputChange}
                  required
                  className="w-full px-4 py-3 bg-muted/50 border border-primary/10 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50"
                  placeholder="your.email@example.com"
                />
              </div>

              <div>
                <label htmlFor="message" className="block text-sm font-medium mb-2">
                  Message
                </label>
                <textarea
                  id="message"
                  name="message"
                  value={formData.message}
                  onChange={handleInputChange}
                  required
                  rows={5}
                  className="w-full px-4 py-3 bg-muted/50 border border-primary/10 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary/50"
                  placeholder="How can we help you with positive thinking?"
                />
              </div>

              <input name="form_name" type="hidden" value={formData.form_name} />
              
              <div className="relative group">
                <div className="absolute -inset-1 rounded-lg blur-md bg-gradient-to-r from-primary to-secondary opacity-70 group-hover:opacity-100 transition-opacity"></div>
                <Button
                  type="submit"
                  disabled={isSubmitting}
                  className="relative w-full py-6 bg-gradient-to-r from-primary to-secondary hover:from-primary/90 hover:to-secondary/90"
                >
                  {isSubmitting ? "Submitting..." : (
                    <span className="flex items-center gap-2">
                      Send Message <Send className="h-4 w-4" />
                    </span>
                  )}
                </Button>
              </div>

              {submitStatus === "success" && (
                <div className="p-4 bg-accent/20 border border-accent/30 text-foreground rounded-lg">
                  <div className="flex items-center gap-2">
                    <Sparkles className="h-5 w-5 text-accent" />
                    <p>Thank you for reaching out! We'll be in touch soon to help you start your positive thinking journey.</p>
                  </div>
                </div>
              )}

              {submitStatus === "error" && (
                <div className="p-4 bg-destructive/20 border border-destructive/30 text-foreground rounded-lg">
                  <p>There was an error submitting the form. Please try again or contact us directly.</p>
                </div>
              )}
            </form>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContactSection;