CXX := g++
CXXFLAGS := -std=c++11 -Wall
SRCS := virtual_init_client.cpp
OBJS := $(SRCS:.cpp=.o)
EXECUTABLE := runVirtualInitClient

$(EXECUTABLE): $(OBJS)
	$(CXX) $(CXXFLAGS) -o $@ $(OBJS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $<

clean:
	rm -f $(OBJS) $(EXECUTABLE)
